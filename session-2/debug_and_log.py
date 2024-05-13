
from utils.logger import logging as logger

def calculate_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    try: 
        average = total / count
    except ZeroDivisionError as e:
        logger.error(f"{str(e)}")
        return 0
    return average

numbers = []
result = calculate_average(numbers)
print("The average is:", result)

# 1. loss of precision because of division
# 2. Division by zero error

# Bug -> inputs -> expected output -> actual output
# Cases -> inputs(create) -> expected output -> actual output

# Properly identifying the error and logging those

# Scenario 1
# fetch list of users from external  API, respond with first 5 names of users

# GET /users/first/5

# API - https://jsonplaceholder.typicode.com/users?_page=2&_limit=5


import requests
# Network Error
# API responding with false data
# API responding with no data

# variations
    # - 200 response
    # - 500 response Server error
    # - 403 response Authorization error
    # - 404 response resource not found
    # - 400 response bad request

# __dict__

# Errors
    # - known errors
    # - syntax errors
    # - exceptions
    # - unknown errors

# Don't rely on try except for all the errors/exceptions
# Never assume things


# response 422
# {
#     "statusCode": 422,
#     "message": "The given data is invalid.",
#     "errors": {
#         "uniqueId": [
#             {
#                 "code": "4227",
#                 "message": "Account doesn't exist with these details."
#             }
#         ]
#     }
# }

DEBUG=False

MAX_ALLOWED_TIME = 60

def fetchUsers(url):
    result = []
    try: 
        if DEBUG:
            response = requests.get(url)
            data = response.json()
        else:
            data = []

        # Handling known error and breaking out the logic
        if response.status_code == 422: 
            # code smell 1 - response format handling
            message = response.json().get("errors", {}).get("uniqueId", [])[0].get("message", "")
            logger.error(f"422: {message}")
            return result
        
       
        # ----------
        # undesired condition 2
        # 3

        if response.status_code == 200:
            if isinstance(data, list):
                result = response.json()[:5]
            else:
                logger.debug(f"422: api response is not an dict")

            return result

    except TimeoutError as e:
        logger.error(f"{str(e)}")
    except Exception as e:
        logger.error(f"{str(e)}")

    return result

url = "https://jsonplaceholder.typicode.com/users"
fetchUsers(url)







