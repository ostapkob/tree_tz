def list_from_dict(data):
    db = []

    def recursive(data, parent=0, level=0):
        level += 1
        for item in data:
            db.append([parent, item['id'], item['alias'], item['name'], level])
            if item.get('childrens') is not None:
                recursive(item.get('childrens'), item['id'], level)

    recursive(data)
    return db
