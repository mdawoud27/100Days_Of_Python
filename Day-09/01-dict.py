#!/usr/bin/python3

# A dictionary is a collection of a key-value pairs.
person = {'height': 172, 'weight': 60, 'eye_color': 'black', 'language': ['arabic', 'english']}

print(person)
print(type(person))  # dict
print(dir(person))
print(len(person))

# print items contains keys and values
print(person.items())
print(person.keys())  # print keys
print(person.values())  # print values

# modifies on dict, dict is mutable can be changed
person['sex'] = 'male'
person['weight'] = 62  # modify on exist key

# can be converted to list ?!
my_list = list(person)
print(my_list)  # prints only keys by default, and we can customize print

print(person['language'][0])  # arabic
print(type(person['language']))  # list

# nested dict
humans = {
    1: {'name': 'Mohamed', 'age': 21, 'language': 'arabic'},
    2: {'name': 'ali', 'age': 22, 'language': 'english'},
    3: {'name': 'dawoud', 'age': 23, 'language': ['arabic', 'english']}
}  # and you can do the previous operations simply
print(humans)
print(humans[3])  # third key and its values
print(humans[3]['name'])  # value of third key at the first index => name: dawoud

# delete using keyword `del`
del humans[2]
print(humans)

del humans[1]['language']  # delete key and its value
print(humans)
