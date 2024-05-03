# Recursive functinos

sum = 0
def natural_sum(n, sum=0) -> int:

    if n == 0:
        return sum
    
    sum = sum + n
    return natural_sum(n-1, sum)

sum = 0
result = natural_sum(5, sum)
print(result)

# Base condition
# Exit Case


nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    },
    'f': 4
}

{
    "a": 1, "a_b_c": 2, "a_b_d_e": 3, "f": 4
}



































def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Example usage:
nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    },
    'f': 4
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)


# isinstance
# list to dict
# dict to list


