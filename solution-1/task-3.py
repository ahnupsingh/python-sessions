# Problem: Write a recursive program to flatten a nested dictionary. The dictionary can be nested to any levels.

def flatten_dict(dictionary: dict, parent_key = '') -> dict:
    """ """
    separator = "_"
    items = []
    for key, value in dictionary.items():
        if parent_key:
            new_key = parent_key + separator + key
        else:
            new_key = key
        
        if type(value) == type({}):
            items.extend(flatten_dict(value, new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)



nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': {
                'g': 4
            }
        }
    },
    'h': 5
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)

