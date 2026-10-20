"""05과정: 파일 읽기와 분리한 하루 계산 예제. 수량은 개, 금액은 원."""


def calculate_day(prepared, requested, unit_price):
    """재고 이월·반품·할인 없음. 입력은 0 이상의 정수만 허용합니다."""
    for name, value in (("준비수량", prepared), ("주문수량", requested), ("가격", unit_price)):
        # bool도 int처럼 취급될 수 있어 정확한 int 자료형만 허용합니다.
        if type(value) is not int or value < 0:
            raise ValueError(f"{name}: 0 이상의 정수여야 합니다.")
    sold = min(prepared, requested)
    return {
        "판매수량": sold,
        "매출": sold * unit_price,
        "남은수량": prepared - sold,
        "못채운주문": requested - sold,
    }


if __name__ == "__main__":
    print(calculate_day(40, 45, 2000))
