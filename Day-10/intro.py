#!/usr/bin/python3

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

name = format_name("MoHaMeD", "DaWOUd")
print(name)