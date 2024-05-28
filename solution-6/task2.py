def calculate_total_price(price, tax_rate):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    if not isinstance(tax_rate, (int, float)):
        raise TypeError("Tax rate must be a number")
    assert price > 0, "Price must be positive"
    assert 0 <= tax_rate <= 1, "Discount must be between 0 and 1"
    total_price = price + (price * tax_rate)
    return total_price


prices = [100, 200, -50, "a"]
tax_rate = 0.07

for price in prices:
    try:
        print(f"Total price: ${calculate_total_price(price, tax_rate)}")
    except Exception as e:
        print(e)
