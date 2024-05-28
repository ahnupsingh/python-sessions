def flatten_dictionary(dictionary: dict, parent_key=""):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}_{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dictionary(value, new_key))
        else:
            flattened_dict[new_key] = value
    return flattened_dict


nested_dict = {
    "key1": {
        "key2": {"key3": "value1"},
        "key4": "value2",
    },
    "key5": {
        "key6": "value3",
        "key7": {
            "key8": {
                "key9": {
                    "key10": "value4",
                },
            }
        },
    },
}

print(flatten_dictionary(nested_dict))
