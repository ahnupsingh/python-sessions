def get_value_or_none(data, key):
    value = data.get(key, None)
    return None if value == 'NA' else value