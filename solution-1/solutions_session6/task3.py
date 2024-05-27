# ## Task 3: Comprehensive Refactoring and Defensive Coding
# Objective: Refactor and apply defensive coding to a more complex function.

# ### Instructions:

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
# print(get_user_data(user_id, user_database), end='\n\n')

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Refactored Code

def get_user_data(user_id: int, user_database: dict) -> dict:
    user_data = user_database.get(user_id, None)
    if not user_data:
        return None
    name = user_data.get('name', 'Unknown')
    age = user_data.get('age', 'Unknown')
    email = user_data.get('email', 'Unknown')
    response = {'name': name, 'age':age, 'email': email}
    return response


user_database = {
    1: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    2: {'name': 'Bob', 'age': 25},
    3: {'email': 'charlie@example.com'}
}
print(get_user_data(2, user_database))