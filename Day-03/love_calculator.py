#!/usr/bin/python3

# TRUE vs LOVE
print('Welcome to the love Calculator!')
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# Convert the names to lower case
name1 = name1.lower()
name2 = name2.lower()

# Combine the 2 names
combine_names = name1.lower() + name2.lower()

# Count TRUE
t = combine_names.count('t')
r = combine_names.count('r')
u = combine_names.count('u')
e = combine_names.count('e')
true = t + r + u + e
print(f'Total = {true}')

# Count LOVE
l = combine_names.count('l')
o = combine_names.count('o')
v = combine_names.count('v')
love = l + o + v + e
print(f'Total = {love}')

# Final Score
score = true * 10 + love
if score == 0:
    print('Kill yourself, man :)')
    exit(0)

print(f'Your Score = {score}')
print(f'Your Score is {score}', end='')
if (score < 10) or (score > 90):
    print(f', you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(', you are alright together.')
else:
    print('.')
