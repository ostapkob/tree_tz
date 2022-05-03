from table_to_json import get_by_level
from rich import print


def recursive_json(json_obj, child, file, deep=100, level=0, url=''):
    childrens = child.get('childrens', None)
    level += 1
    if level> deep:
        return
    url += "/" + child['alias']
    line = '-  '*level + \
        f"{child['id']} : {child['name']} - {url}\n"
    file.write(line)
    if childrens is not None:
        [recursive_json(json_obj, child, file, deep, level, url) for child in childrens]


def json_to_file(data, filename, deep=100):
    if not data:
        print("[red1]json is empty[/red1]")
        return
    with open(filename, 'w') as f:
        for item in data:
            recursive_json(data, item, f, deep)


def recursive_table(table, file, item, level=0, url=''):
    childrens = [x for x in table if x[1] == item[0]]
    level += 1
    url += '/' + item[2]
    line = '*  '*level + \
        f"{item[0]} : {item[3]} - {url}\n"
    file.write(line)
    if childrens:
        [recursive_table(table, file, child, level, url) for child in childrens]


def table_to_file(table, filename):
    if not table:
        print("[red1]tabel is empty[/red1]")
        return
    with open(filename, 'w') as f:
        items = get_by_level(table, 1)
        for item in items:
            recursive_table(table, f,  item)
