#!/usr/bin/python3

student_heights = input("Input a list of student heights ").split()

# The following loop to convert string to int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

# method 1 => using loop
sum_heights = 0
for i in student_heights:
    sum_heights += i

avg = sum_heights / len(student_heights)
print(f'Average of heights with method 1 = {round(avg)}')

# method 2 => using built-in functions
average = sum(student_heights) / len(student_heights)

# finally we print the average
print(f'Average of heights with method 2 = {avg:0.0f}')
