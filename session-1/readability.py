# Tips for writing readable code: meaningful variable names, comments, and code structure

# Avoid single-letter variable names (except for loop counters).
# Bad
x = 5
y = 10
z = x + y

# Good
num1 = 5
num2 = 10
result = num1 + num2


# Write Clear Comments

# Bad: Unnecessary comment
result = num1 + num2  # Add num1 and num2

# Good: Explanation of logic
# Calculate the sum of num1 and num2
result = num1 + num2


# Use Descriptive Function and Method Names
# Bad
def f(a, b):
    return a + b
    
# Good
def add_numbers(num1, num2):
    return num1 + num2


# Keep Functions and Methods Short
    # Functions and methods should ideally do one thing and do it well.


# Avoid Magic Numbers and Strings
# Bad
if x > 3600:
    print("Timeout occurred")

# Good
TIMEOUT_THRESHOLD = 3600
if x > TIMEOUT_THRESHOLD:
    print("Timeout occurred")


# Document Function and Module Purpose
    # Use docstrings to document the purpose, parameters, and return values of functions and methods.

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def greet(name):
    """
    Greet a person by printing a welcome message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None
    """
    print(f"Hello, {name}! Welcome!")

if __name__ == "__main__":
    # Example usage of calculate_rectangle_area function
    rectangle_length = 5
    rectangle_width = 3
    area = calculate_rectangle_area(rectangle_length, rectangle_width)
    print(f"The area of the rectangle is: {area}")

    # Example usage of greet function
    guest_name = "Alice"
    greet(guest_name)
