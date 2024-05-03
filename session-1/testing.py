def add(a, b):
    result = a + b
    print(result)
    return result

# Test cases
assert add(1, 1) == 2, "Positive Integers"
assert add(0, 0) == 0, "Zero values"
assert add(-1, 1) == 0, "Negative and Positive"
assert add(10, -5) == 5, "Positive and Negative"
assert add(-10, -10) == -20, "Negative Integers"
# assert add(10.1, 10.2) == 20.3, "Floating Numbers"
assert add("a", "b") == "ab", "String values"

print("add: All test cases passed successfully!")






































# # Handle error using try except block
# def add2(a, b):
#     try:
#         result = a + b
#         # print(result)
#         return result
#     except:
#         return None

# # assert add2(10.1, 10.2) == 20.30, "Floating Numbers"
# assert add2(None, 10.2) == None, "Null values"
# print("add2: All test cases passed successfully!")






































def add2(a, b):
    try:
        result = a + b
        if isinstance(result, float):
            result = round(result, ndigits=2)

        print(result)
        return result
    except:
        return None

assert add2(10.1, 10.2) == 20.3, "Floating Numbers"
assert add2(None, 10.2) == None, "Null values"
print("add2: All test cases passed successfully!")































def merge_dicts(dict1, dict2) -> dict:
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Test cases
assert merge_dicts({'a': 1, 'b': 2}, {'c': 3}) == {'a': 1, 'b': 2, 'c': 3}, "Basic Test 1"
assert merge_dicts({'x': 10}, {'y': 20, 'z': 30}) == {'x': 10, 'y': 20, 'z': 30}, "Basic Test 2"
assert merge_dicts({'name': 'Alice'}, {'age': 30, 'city': 'New York'}) == {'name': 'Alice', 'age': 30, 'city': 'New York'}, "Test case 3 failed"
assert merge_dicts({}, {'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}, "Empty first dictionary"
assert merge_dicts({'a': 1, 'b': 2}, {}) == {'a': 1, 'b': 2}, "Empty second dictionary"
assert merge_dicts({'key1': 'value1'}, {'key1': 'value2'}) == {'key1': 'value2'}, "Common Keys"
assert merge_dicts({}, {}) == {}, "Both empty dict"

print("merge_dicts: All test cases passed successfully!")







































