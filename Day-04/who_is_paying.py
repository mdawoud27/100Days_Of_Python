#!/usr/bin/python3
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
nameAsCSV = input("Give me everybody's names: ")
names = nameAsCSV.split(", ")

i = random.randint(0, len(names) - 1)
print(f'{names[i]} is going to buy the meal today.')


