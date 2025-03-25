def calculate_total_price(price, tax_rate):
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Invalid price value")
    if not isinstance(tax_rate, (int, float)) or not (0 <= tax_rate <= 1):
        raise ValueError("Invalid tax rate")
    
    total_price = price + (price * tax_rate)
    return total_price

prices = [100, 200, -50, 'a']
tax_rate = 0.07

for price in prices:
    try:
        total = calculate_total_price(price, tax_rate)
        print(f"Total price: ${total:.2f}")
    except ValueError as e:
        print(f"Error calculating total price: {e}")
