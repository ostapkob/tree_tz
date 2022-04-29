def get_by_level(db, level=1):
    items = [x for x in db if x[4] == level]
    return items if items else None


def recursive(db, item):
    _, id, alias, name, _ = item
    childrens = [x for x in db if x[0] == item[1]]
    if childrens:
        return {
            'id': id,
            'alias': alias,
            'name': name,
            'childrens': [recursive(db, child) for child in childrens]
        }
    return {'id': id, 'alias': alias, 'name': name}


def dict_from_list(db, deep=100):
    menu = []
    db = [x for x in db if x[4] <= deep]
    items = get_by_level(db, 1)
    for item in items:
        menu.append(recursive(db, item))
    return menu
