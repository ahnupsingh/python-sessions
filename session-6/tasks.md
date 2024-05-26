## Task 1: Refactoring
Objective: Refactor the provided code snippet to improve readability and maintainability.

### Instructions:

- Identify areas of the code that can be improved.
- Apply refactoring techniques such as renaming variables, extracting functions, simplifying conditional expressions, and removing code duplication.
- Ensure the refactored code produces the same output as the original code.

### Original Code Snippet:

```python
    def process_transactions(transactions):
        for t in transactions:
            if t['type'] == 'credit':
                if t['amount'] > 0:
                    print(f"Credit transaction of ${t['amount']}")
                else:
                    print("Invalid credit amount")
            elif t['type'] == 'debit':
                if t['amount'] > 0:
                    print(f"Debit transaction of ${t['amount']}")
                else:
                    print("Invalid debit amount")
            else:
                print("Unknown transaction type")

    transactions = [
        {'type': 'credit', 'amount': 100},
        {'type': 'debit', 'amount': 50},
        {'type': 'credit', 'amount': -20},
        {'type': 'transfer', 'amount': 30}
    ]

    process_transactions(transactions)
```

process_transactions(transactions)


## Task 2: Defensive Coding
Objective: Apply defensive coding techniques to the provided code snippet to handle potential errors and edge cases.

### Instructions:

- Identify potential issues in the code that could lead to errors or incorrect behavior.
- Implement defensive coding techniques such as input validation, error handling, and assertions.
- Ensure the modified code handles edge cases and produces the correct output.

### Original Code Snippet:
```python
def calculate_total_price(price, tax_rate):
    total_price = price + (price * tax_rate)
    return total_price

prices = [100, 200, -50, 'a']
tax_rate = 0.07

for price in prices:
    print(f"Total price: ${calculate_total_price(price, tax_rate)}")

```

## Task 3: Comprehensive Refactoring and Defensive Coding
Objective: Refactor and apply defensive coding to a more complex function.

### Instructions:

- Refactor the provided code to improve its structure and readability.
- Implement defensive coding techniques to handle potential errors and edge cases.
- Ensure the final code is robust, readable, and produces the correct output.

### Original Code Snippet:
```python
def get_user_data(user_id, user_database):
    if user_id in user_database:
        user_data = user_database[user_id]
        if 'name' in user_data:
            name = user_data['name']
        else:
            name = "Unknown"
        if 'age' in user_data:
            age = user_data['age']
        else:
            age = "Unknown"
        if 'email' in user_data:
            email = user_data['email']
        else:
            email = "Unknown"
        return {'name': name, 'age': age, 'email': email}
    else:
        return None

user_database = {
    1: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    2: {'name': 'Bob', 'age': 25},
    3: {'email': 'charlie@example.com'}
}

user_id = 2
print(get_user_data(user_id, user_database))
```
