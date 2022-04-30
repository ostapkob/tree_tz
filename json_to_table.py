def json_to_table(data):
    db = []

    def recursive(data, parent=0, level=0):
        level += 1
        for item in data:
            db.append([item['id'], parent, item['alias'], item['name'], level])
            if item.get('childrens') is not None:
                recursive(item.get('childrens'), item['id'], level)

    recursive(data)
    return db
