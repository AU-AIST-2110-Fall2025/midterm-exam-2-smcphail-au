# Grading Report

**Final Grade: 9.90/10.00**

## Rubric

| Criterion | Points |
|-----------|--------|
| `extract_data` correctly slices, title-cases names, int conversion, extracts grades, and leaves input untouched | **3** |
| `curve_grades` applies the curve (while loop) and caps values at 100 | **3** |
| `print_top_performers` prints only qualifying `Name: Score` lines (>= 95) | **3** |
| Code quality (required loop choices, clear logic) | **0.9** |

## General Comments

All tests passed and your functions meet the requirements. Combine the two loops in extract_data into a single loop and use clearer variable names to avoid iterating raw_data twice and improve style.

Great job!

## Functionality

- tests/test_grader.py::RosterHelperTests::test_curve_grades_values_and_clamping: Passed (10.0 points)

- tests/test_grader.py::RosterHelperTests::test_extract_data_parses_names_and_grades_title_case: Passed (10.0 points)

- tests/test_grader.py::RosterHelperTests::test_extract_data_returns_new_lists: Passed (10.0 points)

- tests/test_grader.py::RosterHelperTests::test_print_top_performers_prints_name_and_score_for_ge_95: Passed (10.0 points)


