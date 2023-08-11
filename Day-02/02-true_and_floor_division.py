#!/usr/bin/python3

dt = 7 / 4  # 1.75
df = 7 // 4  # 1 .. 1.75 .. 2  => 1 take the least value

dt1 = -13 / 4  # -3.25
df1 = 3 // 5  # 0 .. 0.6 .. 1  => 0 take the least value

df2 = -14 // 7  # -2
df3 = -13 // 4  # -4 .. -3.25 .. -3 => -4

# Exceptions and Tracebacks
# d = 27 / 0  # ZeroDivisionError: division by zero
# print(q + 10)  # NameError: name 'q' is not defined
