#!/usr/bim/python3

student_scores = input("Input a list of student scores ").split()

# The following loop to convert string to int
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

max_score = student_scores[0]
for i in student_scores:
    if i > max_score:
        max_score = i

print(f"Max Score of students = {max_score}")
