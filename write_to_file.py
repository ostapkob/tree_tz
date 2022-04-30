from table_to_json import get_by_level
from rich import print


def recursive_json(data, file, level=0):
    level += 1
    for item in data:
        line = '-  '*level + \
            f"{item['id']}, {item['alias']} : {item['name']} \n"
        file.write(line)

        parent = item.get('childrens', None)
        if parent is not None:
            recursive_json(parent, file,  level)


def json_to_file(data, filename):
    if not data:
        print("[red1]json is empty[/red1]")
        return
    with open(filename, 'w') as f:
        recursive_json(data, f)


def recursive_table(table, file, item, level=0):
    childrens = [x for x in table if x[1] == item[0]]
    level += 1
    line = '*  '*level + \
        f"{item[0]}, {item[2]} : {item[3]} \n"
    file.write(line)
    if childrens:
        [recursive_table(table, file, child, level) for child in childrens]


def table_to_file(table, filename):
    if not table:
        print("[red1]tabel is empty[/red1]")
        return
    with open(filename, 'w') as f:
        items = get_by_level(table, 1)
        for item in items:
            recursive_table(table, f,  item)
