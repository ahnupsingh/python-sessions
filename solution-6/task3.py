def get_user_data(user_id, user_database):
    if not isinstance(user_id, int):
        raise TypeError("User ID must be an integer")

    if not isinstance(user_database, dict):
        raise TypeError("User database must be a dictionary")

    if user_id not in user_database:
        raise Exception("User not found")

    user_data = user_database[user_id]

    return {
        "name": user_data.get("name", "Unknown"),
        "age": user_data.get("age", "Unknown"),
        "email": user_data.get("email", "Unknown"),
    }


user_database = {
    1: {"name": "Alice", "age": 30, "email": "alice@example.com"},
    2: {"name": "Bob", "age": 25},
    3: {"email": "charlie@example.com"},
}

try:
    user_id = 2
    print(get_user_data(user_id, user_database))
except Exception as e:
    print(e)
