# Key principles

# - Input validation
# - Error Handling
# - Code Assertions
# - Fail Safe Defaults
# - Immutability


# - Input Validation
def process_order(order):
    if not isinstance(order, dict):
        raise ValueError("Invalid order format")
    if 'status' not in order:
        raise KeyError("Order status missing")
    

    # Further processing...

# - Error Handing
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"

# - Code Assertion
def calculate_discount(price, discount):
    assert price > 0, "Price must be positive"
    assert 0 <= discount <= 1, "Discount must be between 0 and 1"
    return price * (1 - discount)


# Early return
# Param Validation


