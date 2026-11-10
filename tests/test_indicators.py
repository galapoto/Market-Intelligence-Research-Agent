import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analysis"))
from check_indicators import annual_growth_pct, calculate_growth, load_indicators


class IndicatorTests(unittest.TestCase):
    def test_denmark_fast_charger_growth(self):
        self.assertEqual(annual_growth_pct(1200, 3000), 150.0)

    def test_finland_fast_charger_growth(self):
        self.assertEqual(annual_growth_pct(1300, 2800), 115.38)

    def test_zero_baseline_is_not_silently_divided(self):
        with self.assertRaises(ValueError):
            annual_growth_pct(0, 5)

    def test_csv_parsing(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "d.csv"
            path.write_text("country,charger_type,2020,2021,2022,2023\nDenmark,Fast,560,240,1200,3000\n", encoding="utf-8")
            got = calculate_growth(load_indicators(path))
            self.assertEqual(got[0]["growth_pct"], 150.0)


if __name__ == "__main__":
    unittest.main()
