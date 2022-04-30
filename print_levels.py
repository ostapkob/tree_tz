from rich import print
from dict_from_list import get_by_level


def waves(f):
    def wrap(*args):
        f(*args)
        print("[gold1]~ [/gold1]"*30)
    return wrap


def recursice_dict(data, deep=100, level=0):
    level += 1
    if level > deep:
        return
    for item in data:
        print('-  '*level, item['id'], item['alias'],
              ':', f"[cyan1] {item['name']} [/cyan1]")
        parent = item.get('childrens', None)
        if parent is not None or deep <= level:
            recursice_dict(parent,   deep, level)


@waves
def print_dict_by_levels(db, deep=100):
    recursice_dict(db, deep)


def recursive_list(db, item, level=0):
    childrens = [x for x in db if x[0] == item[1]]
    level += 1
    print("*  " * level, item[1], item[2], ':',
          f"[sky_blue2] {item[3]} [/sky_blue2]")
    if childrens:
        [recursive_list(db, child, level) for child in childrens]


@waves
def print_list_by_levels(db, deep=100):
    db = [x for x in db if x[4] <= deep]
    items = get_by_level(db, 1)
    for item in items:
        recursive_list(db, item)
