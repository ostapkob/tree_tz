import json
from rich import print
from print_levels import *
from list_from_dict import *
from dict_from_list import *
from write_to_file import *

with open('categories_2.json', 'r') as f:
    data = json.load(f)

# print(data)


db = list_from_dict(data)
# print(db)
# print("[gold1]~ [/gold1]"*30)

print_dict_by_levels(data)

menu = dict_from_list(db, 4)
# print(menu)

print_dict_by_levels(menu, 4)

write_to_file(menu)

print_list_by_levels(db, 4)
