from rich import print
from table_to_json import get_by_level
from rich.table import Table
from rich.console import Console


def waves(f):
    def wrap(*args):
        print()
        f(*args)
        print("[gold1]~ [/gold1]"*30)
    return wrap


def recursice_json(data, deep=100, level=0):
    level += 1
    if level > deep:
        return
    for item in data:
        print('🔸  '*level, item['id'], item['alias'],
              ':', f"[cyan1] {item['name']} [/cyan1]")
        childrens = item.get('childrens', None)
        if childrens is not None or deep <= level:
            recursice_json(childrens,   deep, level)


@waves
def print_json_by_levels(data, deep=100):
    if deep<1:
        print("[red1]deep can't be less than 1[/red1]")
        return
    recursice_json(data, deep)


def recursive_table(table, item, level=0):
    childrens = [x for x in table if x[1] == item[0]]
    level += 1
    print("🔹 " * level, item[0], item[2], ':',
          f"[sky_blue2] {item[3]} [/sky_blue2]")
    if childrens:
        [recursive_table(table, child, level) for child in childrens]


@waves
def print_table_by_levels(table, deep=100):
    if not table:
        print("[red1]tabel is empty[/red1]")
        return
    if deep<1:
        print("[red1]deep can't be less than 1[/red1]")
        return
    table = [x for x in table if x[4] <= deep]
    items = get_by_level(table, 1)
    for item in items:
        recursive_table(table, item)


def print_how_table(data):
    if not data:
        print("[red1]tabel is empty[/red1]")
        return
    console = Console()
    table = Table(show_header=True, header_style='bold')
    heders = ['id', 'parent_id', 'alias', 'name', 'level']
    table.add_column('id', style='green1')
    table.add_column('parent_id', style='green3')
    table.add_column('alias', style='sky_blue1')
    table.add_column('name', style='sky_blue3')
    table.add_column('level', style='cyan2')
    for row in data:
        row = [str(x) for x in row]
        table.add_row(*row)
    console.print(table)
