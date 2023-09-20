#!/uer/bin/python3
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Pikachu"])
table.add_column("Type", ["Electric", "Electric"])

print(table)
print()

t = PrettyTable()
t.field_names = ["Pokemon", "Type"]
t.add_row(["Pikachu", "Electric"])
t.add_row(["Pikachu", "Electric"])
t.add_row(["Pikachu", "Electric"])
t.align = 'l'
print(t)
