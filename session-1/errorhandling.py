# Try Except Block
# Pre-defined Exceptions: ValueError, DivisionByZero
# Custom Exceptions


class MinAgeError(Exception):
    def __init__(self, message="Age below minimum required."):
        super().__init__(message)

class MaxAgeError(Exception):
    def __init__(self, message="Age exceeds maximum allowed."):
        super().__init__(message)

def check_voter_eligibility(age):
    min_age = 18
    max_age = 100

    if age < min_age:
        raise MinAgeError
    elif age > max_age:
        raise MaxAgeError
    else:
        print("You are eligible to vote!")

try:
    age = int(input("Enter your age: "))
    check_voter_eligibility(age)
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")
except MinAgeError:
    print("You are not eligible to vote. Minimum age required is 18.")
except MaxAgeError:
    print("You are not eligible to vote. Age exceeds maximum allowed (100 years).")