def find_most_frequent(numbers):
    if numbers:
        count = {}
        for number in numbers:
            count[number] = count.get(number, 0) + 1
        return max(count, key=count.get)
    else:
        return "List is empty"

# Test cases
basic_list = [1, 5, 3, 2, 7, 4, 1, 5, 9, 4, 1, 2, 3, 6, 5, 2, 3, 5, 1, 8, 5]
empty_list = []
multiple_list = [1, 2, 6, 5, 3, 4, 5, 9, 2, 1, 3, 6, 5, 4, 1]
string_list = ["Apple", "Banana", "Apple", "Mango", "Grapes"]

# Test cases
assert find_most_frequent(basic_list) == 5, "Basic Case"
assert find_most_frequent(empty_list) == "List is empty", "Empty List"
assert find_most_frequent([9]) == 9, "List having single element"
assert (
    find_most_frequent(multiple_list) == 5 or find_most_frequent(multiple_list) == 1
), "Multiple most frequent items"
assert find_most_frequent(string_list) == "Apple", "List of strings"

print("find_most_frequent: All test cases passed successfully!")
