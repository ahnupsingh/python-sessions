## Task 3: Comprehensive Refactoring and Defensive Coding
# Objective: Refactor and apply defensive coding to a more complex function.

### Instructions:

# - Refactor the provided code to improve its structure and readability.
# - Implement defensive coding techniques to handle potential errors and edge cases.
# - Ensure the final code is robust, readable, and produces the correct output.

### Original Code Snippet:

# def get_user_data(user_id, user_database):
#     if user_id in user_database:
#         user_data = user_database[user_id]
#         if 'name' in user_data:
#             name = user_data['name']
#         else:
#             name = "Unknown"
#         if 'age' in user_data:
#             age = user_data['age']
#         else:
#             age = "Unknown"
#         if 'email' in user_data:
#             email = user_data['email']
#         else:
#             email = "Unknown"
#         return {'name': name, 'age': age, 'email': email}
#     else:
#         return None


# user_id = 2
# print(get_user_data(user_id, user_database))

user_database = {
    1: {"name": "Alice", "age": 30, "email": "alice@example.com"},
    2: {"name": "Bob", "age": 25},
    3: {"email": "charlie@example.com"},
}


def get_user_data(user_id, user_database):
    if not user_id in user_database:
        raise ValueError("user not found")
    user_data = user_database[user_id]
    name = user_data.get("name", "Unknown")
    age = user_data.get("age", "Unknown")
    email = user_data.get("email", "Unknown")
    return {"name": name, "age": age, "email": email}


try:
    user_id = int(input("enter the id you want to find: "))
    result = get_user_data(user_id, user_database)
except ValueError as ve:
    if "invalid literal" in str(ve):
        print("Please input a valid ID.")
    else:
        print(ve)
except Exception as e:
    print(e)
else:
    print(result)
