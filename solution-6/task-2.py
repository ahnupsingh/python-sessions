# Original question
# - Identify potential issues in the code that could lead to errors or incorrect behavior.
# - Implement defensive coding techniques such as input validation, error handling, and assertions.
# - Ensure the modified code handles edge cases and produces the correct output.


def calculate_total_price(price, tax_rate):
    if not isinstance(tax_rate, int) or tax_rate < 0:
        raise ValueError("tax_rate must be a positive integer")
    total_price = price + (price * tax_rate)
    if total_price < 0:
        raise ValueError("total_price must be positive")


prices = [100, 200, -50, "a"]
tax_rate = 0.07

try:
    for price in prices:
        if not isinstance(price, int):
            raise Exception(f"invalid price {price} in the list")
        print(f"Total price: ${calculate_total_price(price, tax_rate)}")
except Exception as e:
    print(e)


# potential issues that could lead to errors or incorrect behavior
# 1. string and float or int conacatenation could lead to errors
# 2. tax rate can be invalid
# 3. total price can be negative
