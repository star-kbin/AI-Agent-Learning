"""05과정: 손계산 기대값으로 하루 계산을 검증합니다."""

import unittest
from daily_sales import calculate_day


class DailySalesTests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_day(30, 25, 2000), {
            "판매수량": 25, "매출": 50000, "남은수량": 5, "못채운주문": 0,
        })

    def test_shortage(self):
        self.assertEqual(calculate_day(40, 45, 2000), {
            "판매수량": 40, "매출": 80000, "남은수량": 0, "못채운주문": 5,
        })

    def test_zero_prepared(self):
        self.assertEqual(calculate_day(0, 5, 2000), {
            "판매수량": 0, "매출": 0, "남은수량": 0, "못채운주문": 5,
        })

    def test_equal_quantities(self):
        self.assertEqual(calculate_day(5, 5, 2000), {
            "판매수량": 5, "매출": 10000, "남은수량": 0, "못채운주문": 0,
        })

    def test_zero_request_and_price(self):
        self.assertEqual(calculate_day(5, 0, 0), {
            "판매수량": 0, "매출": 0, "남은수량": 5, "못채운주문": 0,
        })

    def test_invalid_inputs(self):
        for value in (-1, 2.5, "2", True, None):
            for index in range(3):
                args = [5, 5, 2000]
                args[index] = value
                with self.subTest(args=args), self.assertRaises(ValueError):
                    calculate_day(*args)

    def test_quantity_conservation(self):
        for prepared in (0, 1, 10):
            for requested in (0, 1, 15):
                result = calculate_day(prepared, requested, 2000)
                self.assertEqual(prepared, result["판매수량"] + result["남은수량"])
                self.assertEqual(requested, result["판매수량"] + result["못채운주문"])


if __name__ == "__main__":
    unittest.main()
