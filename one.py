# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person(name='{self.name}', age={self.age})"

# person = Person("Alice", 30)
# print(str(person))
# # Output: Person(name='Alice', age=30)
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

# point = Point(3, 4)
# print(repr(point))
# # Output: Point(3, 4)

# import datetime

# today = datetime.date.today()

# # Using str()
# print(str(today))  # Output: 2024-05-14

# # Using repr()
# print(repr(today))  # Output: datetime.date(2024, 5, 14)



import logging

# Define custom format with custom placeholders
format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - Custom1: %(custom1)s - Custom2: %(custom2)s'

# Configure logging with custom format
logging.basicConfig(level=logging.DEBUG, format=format_str)

# Create a logger
logger = logging.getLogger('example_logger')

# Log a message with custom parameters
logger.info('This is a log message with custom parameters', extra={'custom1': 'value1', 'custom2': 'value2'})
