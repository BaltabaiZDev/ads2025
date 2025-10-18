grade_to_point = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0.00
}

n = int(input().strip())
students = []

for _ in range(n):
    data = input().split()
    lastname, firstname = data[0], data[1]
    subj_count = int(data[2])
    grades = data[3:]

    total_points = 0
    total_credits = 0

    for i in range(0, subj_count * 2, 2):
        grade = grades[i]
        credit = int(grades[i + 1])
        total_points += grade_to_point[grade] * credit
        total_credits += credit

    gpa = total_points / total_credits if total_credits > 0 else 0
    students.append((lastname, firstname, gpa))

# Sort: by GPA ascending, then lastname, then firstname
students.sort(key=lambda x: (x[2], x[0], x[1]))

# Print
for ln, fn, gpa in students:
    print(f"{ln} {fn} {gpa:.3f}")