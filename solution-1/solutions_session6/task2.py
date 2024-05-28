# Task 2: Defensive Coding
# Objective: Apply defensive coding techniques to the provided code snippet to handle potential errors and edge cases.

# ### Instructions:

# - Identify potential issues in the code that could lead to errors or incorrect behavior.
# - Implement defensive coding techniques such as input validation, error handling, and assertions.
# - Ensure the modified code handles edge cases and produces the correct output.

### Original Code Snippet:

# def calculate_total_price(price, tax_rate):
#     total_price = price + (price * tax_rate)
#     return total_price

# prices = [100, 200, -50, 'a']
# tax_rate = 0.07

# for price in prices:
#     print(f"Total price: ${calculate_total_price(price, tax_rate)}")


# -------------------------------------------------------------------------------------------------------------------------------
# Refactored code 

class PriceService():

    def calculate_total_price(self, price: float, tax_rate: float) -> float:
        if not self.is_price_valid(price):
            return self.handle_invalid_price()
        if not self.is_taxrate_valid(tax_rate):
            return self.handle_invalid_taxrate()
        print(price, tax_rate)
        total_price = price + (price * tax_rate/100)
        print(f"Total Price: {total_price}")
        return total_price
    
    def is_price_valid(self, price: float) -> bool:
        is_number = isinstance(price, float) or isinstance(price, int)
        is_greater_than_zero = (int(price) > 0)
        return is_number and is_greater_than_zero

    def is_taxrate_valid(self, tax_rate: float):
        return isinstance(tax_rate, float) or isinstance(tax_rate, int)

    @staticmethod
    def handle_invalid_price() -> None:
        print("Price is invalid")
        return None
    
    def handle_invalid_taxrate() -> None:
        print("Tax Rate is invalid")
        return None
    
service = PriceService()
service.calculate_total_price(100, 10)