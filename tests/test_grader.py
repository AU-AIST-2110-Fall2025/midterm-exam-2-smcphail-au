import contextlib
import importlib
import io
import sys
import unittest


def _import_grader():
    if "grader" in sys.modules:
        del sys.modules["grader"]
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        module = importlib.import_module("grader")
    return module


class RosterHelperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grader = _import_grader()

    def test_extract_data_parses_names_and_grades_title_case(self):
        raw_records = [
            "2025-fall:ana lopez:78",
            "2025-fall:priya singh:97",
        ]
        expected_names = ["Ana Lopez", "Priya Singh"]
        expected_grades = [78, 97]

        names, grades = self.grader.extract_data(raw_records)

        self.assertEqual(names, expected_names)
        self.assertEqual(grades, expected_grades)
        # input remains unchanged
        self.assertEqual(
            raw_records,
            [
                "2025-fall:ana lopez:78",
                "2025-fall:priya singh:97",
            ],
        )

    def test_extract_data_returns_new_lists(self):
        raw_records = ["2025-fall:max jones:85"]
        names, grades = self.grader.extract_data(raw_records)

        self.assertIsInstance(names, list)
        self.assertIsInstance(grades, list)
        self.assertEqual(names, ["Max Jones"])
        self.assertEqual(grades, [85])

    def test_curve_grades_values_and_clamping(self):
        grades = [92, 99, 45]
        curved = self.grader.curve_grades(grades, 8)

        # value correctness (identity not required)
        self.assertEqual(curved, [100, 100, 53])

    def test_print_top_performers_prints_name_and_score_for_ge_95(self):
        names = ["Anna", "Ben", "Cara", "Doug", "Elle"]
        scores = [70, 95, 88, 100, 92]

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.grader.print_top_performers(names, scores)

        self.assertEqual(
            buffer.getvalue().strip().splitlines(),
            ["Ben: 95", "Doug: 100"],
        )


if __name__ == "__main__":
    unittest.main()
