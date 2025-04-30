# Most frequently repeating number
from typing import List
def find_most_frequent(numbers: List[int]) -> int:
    """ """
    count_of_numbers = {}
    for number in numbers:
        count_of_numbers[number] = count_of_numbers.get(number, 0) + 1
    
    max_count_number = None
    max_count = 0
    for key, value in count_of_numbers.items():
        if value > max_count:
            max_count_number = key
            max_count = value
    return max_count_number

result = find_most_frequent([2,2,1,1,3,3, 3])
print(result)


# Tests 
assert find_most_frequent([1,2,1]) == 1, "One integer is most repeating"
assert find_most_frequent([1,1,2,2,3]) == 1, "Two integers are most repeating"
assert find_most_frequent([]) == None, "Empty List"