import json
from rich import print
from print_data import *
from json_to_table import *
from table_to_json import *
from write_to_file import *
from postres import *

'''
json -> table -> postres -> table -> json -> levels -> file
'''

with open('categories_2.json', 'r') as f:
    json_obj = json.load(f)

print(json_obj)


table_menu = json_to_table(json_obj)
print(table_menu)
print_how_table(table_menu)

drop_table()
create_table()
insert_items(table_menu)

db_menu = select_items()

print(db_menu)
print_how_table(db_menu)

print_json_by_levels(json_obj)

json_menu = table_to_json(db_menu, 4)
print(json_menu)

json_to_file(json_menu, 'new_file.txt')
table_to_file(db_menu, 'new_file.txt')

print_table_by_levels(db_menu, 4)
print_json_by_levels(json_menu, 4)
