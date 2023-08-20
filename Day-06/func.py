# functions is block of code to perform a task

# def func(name='dawoud'):
#     print(f'welcome to python {name.title()}')
#
# func()

# def full_name(fname, lname, mname = ''):
#     """prints out klfajfka fklasdj;akffa ijjfa;klsd j;jfoas
#     kdsajf;lka fajskl; kljfasl jfsla jf;l a  jal f;s"""
#     if mname:
#         fname = f'{fname.title()} {mname.title()} {lname.title()}'
#     else:
#         fname = f'{fname.title()} {lname.title()}'
#     return fname
#
# # print(full_name('mohamed', 'dawoud'))

# argus list
# def average(*argv):
#     return sum(argv) / len(argv)
#
# avarage = (1, 2, 3, 4, 5)
# print(average(1, 2, 3, 4, 5))

x = 27


# def func():
#     """This is a docstring discribe what the function do
#     in general, that it is"""
#     global x
#     x = 'hello'
#     print(f'value of x = {x}')
# func()

def cube(number):
    return number ** 3


my_list = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 3, my_list))

print(result)

li = ['mohamed mad', 'ali dawoud', 'dawoud ahmed']
li.sort(key=lambda name: name.split(' ')[-1])

print(li)