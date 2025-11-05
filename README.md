# Midterm 2 Practical Exam - Roster Helpers

The AIST-2110 instructor is preparing the final grade reviews and needs to perform some grade corrections and generate a snapshot of the standout students. Unfortunately, the LMS dumped every record in a messy list of strings carrying the term, a lowercase student name, and the grade information. 

Here's the raw data you'll work with:

```python
roster_records = [
    "2025-fall:ana lopez:78",
    "2025-fall:priya singh:97",
    "2025-fall:max jones:85",
    "2025-fall:li chen:88",
    "2025-fall:zoe brown:73",
    "2025-fall:nico garcia:81",
    "2025-fall:minh nguyen:90",
    "2025-fall:carla perez:84",
    "2025-fall:noel davis:76",
    "2025-fall:hana kim:96",
    "2025-fall:ravi patel:69",
    "2025-fall:jade morgan:87",
    "2025-fall:eli smith:82",
    "2025-fall:aria reed:91",
    "2025-fall:theo allen:77",
]
```

YOUR TASK: Implement a Python script to automate the data extraction and perform a report on the top performer students. The starter script `grader.py` already has the exported LMS data.

## Roster Format Assumptions
- `roster_records` is a list of records in string format.
- Every raw record follows `2025-fall:<name>:<two-digit grade>`.
- The prefix `2025-fall:` always has the same length, 
- The final 2 digits contains the grade. Assume that raw exports hold only two-digit grades (no 100 in the `roster_records`).
  - You can rely on these positions when slicing, or you may use `.split()` to parse the fields.

## Workflow Overview

1. **Extract names and grades** - Build a names list (title-cased) and a grades list (ints) from the roster (function `extract_data`).
2. **Curve every numeric grade** - Adjust each score while capping at 100 (function `curve_grades`).
3. **Print standouts** - Print each record with a score at or above 95 (function `print_top_performers`).

## Step 1. `extract_data(raw_data)` (3 pts)

- Populate the two given lists `s_names` and `s_grades` with the formatted names and integer grades.
- Iterate through `raw_data` (the roster strings).
- Use slicing or `.split()` to extract:
  - the student name between the two colons, then convert to title case (e.g., `"ana lopez"` -> `"Ana Lopez"`).
  - the grade from the last two characters, then convert to `int` using the `int()` function.
- Do not modify `raw_data`.
- Return the two new lists: `(s_names, s_grades)`.
- **Expected output:**
  - `s_names`: 
  `["Ana Lopez", "Priya Singh", "Max Jones", "Li Chen", "Zoe Brown", "Nico Garcia", "Minh Nguyen", "Carla Perez", "Noel Davis", "Hana Kim", "Ravi Patel", "Jade Morgan", "Eli Smith", "Aria Reed", "Theo Allen"]`.
  
  - `s_grades`:
    `[78, 97, 85, 88, 73, 81, 90, 84, 76, 96, 69, 87, 82, 91, 77]`.

```
raw_data[i]                    s_names                     s_grades
0 :  2025-fall:ana lopez:78    ->   0 :  Ana Lopez    ->   0 :  78
1 :  2025-fall:priya singh:97  ->   1 :  Priya Singh  ->   1 :  97
2 :  2025-fall:max jones:85    ->   2 :  Max Jones    ->   2 :  85
3 :  2025-fall:li chen:88      ->   3 :  Li Chen      ->   3 :  88
.
.
.
```

> NOTICE: The lists produced by your helpers must remain aligned by index. Index `i` refers to the same student across `raw_data`, the extracted `s_names`, and the extracted `s_grades`.


## Step 2. `curve_grades(grades, by_amount)` (3 pts)
- Loop through the list of grades and add the provided `by_amount` value to each entry.
  - Use a `while` loop to iterate by index for full credit (a `for` loop works but loses style credit).
- Clamp any value above 100 down to 100.
- Return the list of curved grades (return the original list if you modified it).
- Curves can produce three digits such as 100.
- You may either modify the incoming list in place or build and return a new list. Both are acceptable.
- **Expected output:** Starting from the provided grades and using `by_amount = 5`, the resulting list is:   
  `[83, 100, 90, 93, 78, 86, 95, 89, 81, 100, 74, 92, 87, 96, 82]`.

> Notice that the grade in index 1 is clamped to 100 since 97+5 would result in a value larger than 100. 

>Be sure to use the `by_amount` parameter instead of hard-coding a specific value.

## Step 3. `print_top_performers(names, grades)` (3 pts)

- Iterate the names and grades in index order.
- For every grade that is greater than or equal to 95, print one line exactly as `"Name: Score"`.
- The generated output must contain no extra spaces before or after each line.
- **Expected output:** Using the curved list from Step 2, the function should print:
  ```
  Priya Singh: 100
  Minh Nguyen: 95
  Hana Kim: 100
  Aria Reed: 96
  ```


## Rubric

| Criterion | Points |
|-----------|--------|
| `extract_data` correctly slices, title-cases names, int conversion, extracts grades, and leaves input untouched | **3** |
| `curve_grades` applies the curve (while loop) and caps values at 100 | **3** |
| `print_top_performers` prints only qualifying `Name: Score` lines (>= 95) | **3** |
| Code quality (required loop choices, clear logic) | **1** |
| **Total** | **10** |

## How to Test

1. Click the testing beaker icon in VS Code.
2. Locate and run the grade calculator test.
3. Green = pass, Red = check error messages.

## How to Submit

Most of you will now choose to use the VSCode Source Control extension to submit your assignments. However, you can always use the terminal.

- Use the VS code Source Control Tab to submit your assignment:
    - Click the + next to the list of "Changes" to stage all changes that you have made.
    - Write a commit message, e.g., "Finished with midterm 2".
      > _**YOU MUST SUPPLY A COMMIT MESSAGE OR YOU WILL GET ERRORS THAT YOU MAY OR MAY NOT EVEN NOTICE**_
    - Click "Commit".
    - Click "Sync".
      > Or, instead of clicking "Commit" in the previous step, click the down arrow and select Commit & Push.

- Alternatively, you can use git to add, commit, and push your changes. Make sure you are in your `midterm2-yourusername` folder. `cd` your way there if not. Then type:

  ```bash
  git add .
  git commit -m "Finished with midterm 2"
  git push
  ```
