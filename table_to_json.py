from rich import print
def get_by_level(table, level=1):
    items = [x for x in table if x[4] == level]
    return items if items else None


def recursive(table, item):
    id, _, alias, name, _ = item
    childrens = [x for x in table if x[1] == item[0]]
    if childrens:
        return {
            'id': id,
            'alias': alias,
            'name': name,
            'childrens': [recursive(table, child) for child in childrens]
        }
    return {'id': id, 'alias': alias, 'name': name}


def table_to_json(table, deep=100):
    if not table:
        print("[red1]tabel is empty[/red1]")
        return
    if deep<1:
        print("[red1]deep can't be less than 1[/red1]")
        return
    menu = []
    table = [x for x in table if x[4] <= deep]
    items = get_by_level(table, 1)
    for item in items:
        menu.append(recursive(table, item))
    return menu
