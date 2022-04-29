def print_dict_by_levels(data, level=0):
    level += 1
    for item in data:
        print('-  '*level, item['id'], item['alias'], ':', item['name'])
        parent = item.get('childrens', None)
        if parent is not None:
            print_dict_by_levels(parent,  level)
