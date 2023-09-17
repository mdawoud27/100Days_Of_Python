#!/usr/bin/python3

student = {
    "name": "dawoud",
    "age": 21,
    "class": "SCE-3"
}

# Retrieving items from dictionary.
print(student["name"])

# Adding new items to dictionary.
student["status"] = True

print(student)

# create an empty dictionary.
empty_dict = {}

# Edit an item in a dictionary
student["status"] = False
print(student)

# Loop throgh a dictionary
for key, value in student.items():
    print(f"{key} -> {value}")