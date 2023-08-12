#!/usr/bin/python3

row1 = [0, 0, 0]
row2 = [0, 0, 0]
row3 = [0, 0, 0]
t_map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('What do you want put the treasure? ')

horizontal = int(position[0])
vertical = int(position[1])

t_map[horizontal - 1][vertical - 1] = 'x'
print(f'{row1}\n{row2}\n{row3}')
