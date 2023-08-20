#!/usr/bin/python3

bool_true = 27 >= 27
bool_false = 0 != 0

print(bool_true)
print(not bool_true)
print(not (not bool_true))  # True

print(bool_true and bool_false)  # False
print(bool_true or bool_false)  # True
