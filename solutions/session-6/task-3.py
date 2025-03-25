def get_user_data(user_id, user_database):
    if not isinstance(user_id, int):
        raise ValueError("User ID must be an integer")
    
    user_data = user_database.get(user_id)
    if user_data is None:
        return None

    def get_value(data, key, default="Unknown"):
        return data.get(key, default)
    
    name = get_value(user_data, 'name')
    age = get_value(user_data, 'age')
    email = get_value(user_data, 'email')
    
    return {'name': name, 'age': age, 'email': email}

user_database = {
    1: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    2: {'name': 'Bob', 'age': 25},
    3: {'email': 'charlie@example.com'}
}

user_id = 2
try:
    print(get_user_data(user_id, user_database))
except ValueError as e:
    print(f"Error: {e}")
