def recursive(data, file, level=0):
    level += 1
    for item in data:
        line = '-  '*level + \
            f"{item['id']}, {item['alias']} : {item['name']} \n"
        file.write(line)

        parent = item.get('childrens', None)
        if parent is not None:
            recursive(parent, file,  level)


def write_to_file(data):
    with open('new_file', 'w') as f:
        recursive(data, f)
