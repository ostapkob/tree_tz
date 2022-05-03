from rich import print
from table_to_json import get_by_level
from rich.table import Table
from rich.console import Console


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


def recursice_json(json_obj, child, deep=100, level=0, url=''):
    childrens = child.get('childrens', None)
    level += 1
    if level > deep:
        return
    url += '/' + child['alias']
    print('🔸  '*level, child['id'],
          ':', f"[cyan1] {child['name']} [/cyan1], {url}")

    if childrens is not None:
        [recursice_json(json_obj, child, deep, level, url)
         for child in childrens]


@waves
def print_json_by_levels(data, deep=100):
    if deep < 1:
        print("[red1]deep can't be less than 1[/red1]")
        return
    for item in data:
        recursice_json(data, item, deep)


def recursive_table(table, item, level=0,  url=''):
    childrens = [x for x in table if x[1] == item[0]]
    level += 1
    url += '/'+item[2]
    print("🔹 " * level, item[0], ':',
          f"[sky_blue2] {item[3]} [/sky_blue2] - {url}")
    if childrens:
        [recursive_table(table, child, level, url) for child in childrens]


@waves
def print_table_by_levels(table, deep=100):
    if not table:
        print("[red1]tabel is empty[/red1]")
        return
    if deep < 1:
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
    table.add_column('id', style='green1')
    table.add_column('parent_id', style='green3')
    table.add_column('alias', style='sky_blue1')
    table.add_column('name', style='sky_blue3')
    table.add_column('level', style='cyan2')
    for row in data:
        row = [str(x) for x in row]
        table.add_row(*row)
    console.print(table)
