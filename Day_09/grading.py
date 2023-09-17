#!/usr/bin/python3

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}
for key, value in student_scores.items():
    if value >= 91:
        student_grades[key] = "Outstanding"
    elif 81 <= value <= 90:
        student_grades[key] = "Exceed Expectations"
    elif 71 <= value <= 80:
        student_grades[key] = "Acceptable"
    elif value <= 71:
        student_grades[key] = "Fail"

print(student_grades)