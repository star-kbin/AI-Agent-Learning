"""가상 모델의 수치·단위·위반·저장 결과를 확인합니다."""

import tempfile
import unittest
from pathlib import Path
from simulate import BASE, read_csv, save_csv, simulate, verify_saved


class V2GTests(unittest.TestCase):
    def setUp(self):
        self.rows = read_csv(BASE / "sample.csv")

    def test_baseline_and_persisted_result(self):
        results = simulate(self.rows)
        self.assertEqual([r["종료저장량_kWh"] for r in results], [28, 32, 28, 24])
        self.assertEqual(results[-1]["누적거래수지_원"], 960)
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "result.csv"
            save_csv(output, results)
            verify_saved(output, BASE / "expected.csv")
            # 저장값을 일부러 바꾸어 불일치도 잡아내는지 확인합니다.
            results[0]["SOC_pct"] = 99
            save_csv(output, results)
            with self.assertRaises(ValueError):
                verify_saved(output, BASE / "expected.csv")

    def test_idle_comparison(self):
        for row in self.rows:
            row["전력_kW"] = "0"
        results = simulate(self.rows)
        self.assertEqual(results[-1]["종료저장량_kWh"], 24)
        self.assertEqual(results[-1]["누적거래수지_원"], 0)

    def test_price_change(self):
        self.rows[-1]["단가_원_kWh"] = "120"
        self.assertEqual(simulate(self.rows)[-1]["누적거래수지_원"], 560)

    def test_half_hour_units(self):
        rows = [{"구간": "1", "시간_h": "0.5", "단가_원_kWh": "90", "전력_kW": "4"}]
        result = simulate(rows, initial=20, target=22)[0]
        self.assertEqual(result["에너지변화_kWh"], 2)
        self.assertEqual(result["거래수지_원"], -180)
        self.assertAlmostEqual(result["SOC_pct"], 55)

    def test_power_limit(self):
        self.rows[0]["전력_kW"] = "5"
        with self.assertRaisesRegex(ValueError, "전력 상한"):
            simulate(self.rows)

    def test_upper_and_lower_storage(self):
        with self.assertRaisesRegex(ValueError, "저장량 범위"):
            simulate(self.rows, initial=36)
        self.rows[0]["전력_kW"] = "-4"
        with self.assertRaisesRegex(ValueError, "저장량 범위"):
            simulate(self.rows, initial=8)

    def test_final_target(self):
        self.rows[-1]["전력_kW"] = "0"
        with self.assertRaisesRegex(ValueError, "종료 목표"):
            simulate(self.rows)

    def test_discharge_only_not_comparable(self):
        for row in self.rows:
            row["전력_kW"] = "-4"
        with self.assertRaisesRegex(ValueError, "종료 목표"):
            simulate(self.rows)
        result = simulate(self.rows, target=8)[-1]
        self.assertEqual(result["누적거래수지_원"], 2400)
        self.assertEqual(result["종료저장량_kWh"], 8)

    def test_invalid_values(self):
        for field, value in (("시간_h", "0"), ("시간_h", "-1"),
                             ("단가_원_kWh", "-1"), ("전력_kW", "nan"),
                             ("전력_kW", "inf"), ("전력_kW", "문자")):
            rows = [dict(row) for row in self.rows]
            rows[0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                simulate(rows)

    def test_empty_missing_or_duplicate(self):
        with self.assertRaises(ValueError):
            simulate([])
        with self.assertRaises(ValueError):
            simulate([{"구간": "1"}])
        self.rows[1]["구간"] = "1"
        with self.assertRaises(ValueError):
            simulate(self.rows)


if __name__ == "__main__":
    unittest.main()
