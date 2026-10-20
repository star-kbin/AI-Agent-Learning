"""06과정: 효율100%, 주행0의 가상 V2G 손계산을 확인합니다."""

import csv
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
FIELDS = ["구간", "에너지변화_kWh", "종료저장량_kWh", "SOC_pct", "거래수지_원", "누적거래수지_원"]


def finite_number(value, name):
    """NaN·무한대 등 비교를 빠져나갈 수 있는 값도 제외합니다."""
    try:
        if isinstance(value, bool):
            raise ValueError
        number = float(value)
        if not math.isfinite(number):
            raise ValueError
        return number
    except (ValueError, TypeError) as error:
        raise ValueError(f"{name}: 유한한 숫자가 필요합니다.") from error


def simulate(rows, initial=24, capacity=40, minimum=8, maximum=36,
             max_power=4, target=24):
    """각 행의 전력·저장량을 검증합니다. 종료 목표 미달도 거절합니다."""
    initial, capacity, minimum, maximum, max_power, target = [
        finite_number(value, name) for name, value in (
            ("초기 저장량", initial), ("용량", capacity), ("하한", minimum),
            ("상한", maximum), ("최대 전력", max_power), ("종료 목표", target),
        )
    ]
    if not (capacity > 0 and 0 <= minimum <= maximum <= capacity
            and minimum <= initial <= maximum and minimum <= target <= maximum
            and max_power > 0):
        raise ValueError("배터리 설정의 범위를 확인하세요.")
    energy, cash = initial, 0.0
    charged = discharged = 0.0
    results = []
    for index, row in enumerate(rows, 1):
        try:
            duration = finite_number(row["시간_h"], "시간")
            price = finite_number(row["단가_원_kWh"], "단가")
            power = finite_number(row["전력_kW"], "전력")
            period = row["구간"]
        except KeyError as error:
            raise ValueError(f"필수 열 누락: {error.args[0]}") from error
        if str(period) != str(index):
            raise ValueError("구간은 1부터 순서대로 한 행씩 입력하세요.")
        if duration <= 0 or price < 0:
            raise ValueError(f"{period}구간: 시간은 양수, 단가는 0 이상이어야 합니다.")
        if abs(power) > max_power:
            raise ValueError(f"{period}구간: 전력 상한 위반")
        # 양수 충전 / 음수 방전, 효율100%이므로 전력×시간을 그대로 반영합니다.
        delta = power * duration
        energy += delta
        if not minimum <= energy <= maximum:
            raise ValueError(f"{period}구간: 저장량 범위 위반")
        charged += max(delta, 0)
        discharged += max(-delta, 0)
        balance = -delta * price
        cash += balance
        if not all(math.isfinite(v) for v in (delta, energy, balance, cash)):
            raise ValueError("계산값이 유한한 범위를 벗어났습니다.")
        results.append(dict(zip(FIELDS, (str(period), delta, energy,
                                       energy / capacity * 100, balance, cash))))
    if not results:
        raise ValueError("계산할 구간이 없습니다.")
    if not math.isclose(initial + charged - discharged, energy, abs_tol=1e-9):
        raise ValueError("에너지 보존 확인 실패")
    if not math.isclose(energy, target, abs_tol=1e-9):
        raise ValueError(f"종료 목표 불일치: {energy:g} kWh (목표 {target:g})")
    return results


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def save_csv(path, rows):
    with Path(path).open("w", encoding="utf-8", newline="") as target_file:
        writer = csv.DictWriter(target_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def verify_saved(actual_path, expected_path):
    """메모리 결과가 아니라 저장된 파일을 다시 읽어 기대값과 비교합니다."""
    actual, expected = read_csv(actual_path), read_csv(expected_path)
    if len(actual) != len(expected):
        raise ValueError("저장 결과의 행 수 불일치")
    for actual_row, expected_row in zip(actual, expected):
        if actual_row["구간"] != expected_row["구간"]:
            raise ValueError("저장 결과의 구간 불일치")
        for field in FIELDS[1:]:
            actual_number = finite_number(actual_row[field], field)
            expected_number = finite_number(expected_row[field], field)
            if not math.isclose(actual_number, expected_number, rel_tol=1e-9, abs_tol=1e-9):
                raise ValueError(f"저장 결과 불일치: {field}")


if __name__ == "__main__":
    results = simulate(read_csv(BASE / "sample.csv"))
    save_csv(BASE / "result.csv", results)
    verify_saved(BASE / "result.csv", BASE / "expected.csv")
    print(f"종료 저장량: {results[-1]['종료저장량_kWh']:g} kWh")
    print(f"거래수지: {results[-1]['누적거래수지_원']:g} 원")
    print("저장 결과 검증: 일치 (result.csv / expected.csv)")
