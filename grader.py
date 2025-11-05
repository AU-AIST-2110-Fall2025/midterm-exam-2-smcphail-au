
def extract_data(raw_data):
    """
    Return two new lists: title-cased s_names and integer s_grades using the raw roster layout.

    - Use slicing or ``.split()`` (see the README assumptions) to extract:
        - the student name between the two colons, then convert to title case (e.g., ``"ana lopez"`` -> ``"Ana Lopez"``).
        - the two-digit grade at the end of the raw record, then convert to ``int`` using the ``int()`` function.
    TIP: Because names are variable-length, negative slicing is useful both for the grade  and for getting 'to the end of' the name portion.
                        
    Do not modify ``raw_data``.
    Returns: (s_names, s_grades). 
    """
    s_names = []
    s_grades = []

    # ADD YOUR CODE HERE
    for raw in raw_data:
        clean_names = raw.split(':')[1]
        clean_names = clean_names.title()
        s_names.append(clean_names)
    
    for again in raw_data:
        clean_numbers = int(again.split(':')[2])
        s_grades.append(clean_numbers)

    return s_names, s_grades

def curve_grades(grades, by_amount):
    """
    Add ``by_amount`` to every grade, clamping any value above 100 down to 100.

    Use a ``while`` loop for iteration to earn full credit (a ``for`` loop works but loses style credit).
    Return the list containing the curved grades (same list if modified, otherwise new).
    """
    # ADD YOUR CODE HERE
    i = 0
    while i < len(grades):
        added = grades[i] + by_amount
        if added > 100:
            added = 100
        grades[i] = added
        i += 1
    return grades

def print_top_performers(names, grades):
    """
    Print one 'Name: Score' line for each record whose grade is >= 95.

    Iterate the names and grades in index order and, for every grade >= 95, print:
        print(f"{<name>}: {<grade>}")
        replace <name> and <grade> with the correct variable information.
    Output one line per qualifying record, no extra spaces or blank lines.
    Returns: None
    """
    # ADD YOUR CODE HERE
    for i in range(len(grades)):
        if grades[i] >= 95:
            print(f"{names[i]}: {grades[i]}")

def main():


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

    names, grades = extract_data(roster_records)

    # If you were unable to correctly extract the names and grades from roster_records,
    # uncomment the lists below so you can use the formatted data in the next function
    # names = ["Ana Lopez", "Priya Singh", "Max Jones", "Li Chen", "Zoe Brown", "Nico Garcia", "Minh Nguyen", "Carla Perez", "Noel Davis", "Hana Kim", "Ravi Patel", "Jade Morgan", "Eli Smith", "Aria Reed", "Theo Allen"]
    # grades = [78, 97, 85, 88, 73, 81, 90, 84, 76, 96, 69, 87, 82, 91, 77]

    updated_grades = curve_grades(grades, 5)
    
    # If you were unable to correctly curve the grades,
    # uncomment the list below so you can use the curved grades in the next function
    # updated_grades = [83, 100, 90, 93, 78, 86, 95, 89, 81, 100, 74, 92, 87, 96, 82]
    
    print_top_performers(names, updated_grades)


if __name__ == "__main__":
    main()





