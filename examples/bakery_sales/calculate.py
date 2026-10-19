"""교육용 가상 빵가게 기록을 계산합니다. 외부 패키지는 필요하지 않습니다."""

import csv
from pathlib import Path


def summarize(csv_path):
    """수량은 개, 가격과 매출은 원입니다. 재고 이월·반품·할인은 없습니다."""
    result = {"판매수량": 0, "매출": 0, "남은수량": 0, "못채운주문": 0}
    with Path(csv_path).open(encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source)
        required = {"날짜", "준비수량", "주문수량", "판매수량", "개당가격"}
        if not required.issubset(rows.fieldnames or []):
            raise ValueError("필수 열이 빠졌습니다. README의 열 이름을 확인하세요.")
        count = 0
        for row in rows:
            count += 1
            prepared = int(row["준비수량"])
            requested = int(row["주문수량"])
            sold = int(row["판매수량"])
            unit_price = int(row["개당가격"])
            if min(prepared, requested, sold, unit_price) < 0:
                raise ValueError(f"{row['날짜']}: 수량과 가격은 음수일 수 없습니다.")
            if sold != min(prepared, requested):
                raise ValueError(f"{row['날짜']}: 이 예제에서는 판매수량이 준비·주문 중 작은 값이어야 합니다.")
            result["판매수량"] += sold
            result["매출"] += sold * unit_price
            result["남은수량"] += prepared - sold
            result["못채운주문"] += requested - sold
        if count == 0:
            raise ValueError("계산할 행 데이터가 없습니다.")
    return result


if __name__ == "__main__":
    # 파일을 어디서 실행하든 같은 폴더의 sample.csv를 읽습니다.
    totals = summarize(Path(__file__).with_name("sample.csv"))
    print(f"총 판매 수량: {totals['판매수량']:,}개")
    print(f"총 매출: {totals['매출']:,}원")
    print(f"일별 남은 빵 합계: {totals['남은수량']:,}개")
    print(f"못 채운 주문 수량: {totals['못채운주문']:,}개")
