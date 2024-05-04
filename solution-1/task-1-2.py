


def find_most_frequent(numbers):
    if numbers:
        count = {}
        for number in numbers:
            count[number] = count.get(number, 0) + 1
        return max(count, key=count.get)
    else:
        return "List is empty"


