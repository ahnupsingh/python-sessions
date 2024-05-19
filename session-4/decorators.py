# Introduction to Decorators	15	
    # What are decorators?		
    # Importance of decorators in Python programming.		
    # Overview of decorator syntax and usage.			
		
# Creating and Using Decorators	20	
    # Writing simple decorators: without arguments.		
    # Applying decorators to functions: using @ syntax.		
    # Chaining decorators: applying multiple decorators to a single function.		
		
# Decorators with Arguments 	20	
    # Defining decorators with arguments.		
    # Passing arguments to decorators.		
    # Handling arguments within decorators.		
		
# Class Decorators	15	
    # Using classes as decorators.		
    # Implementing call() method in class decorators.		
    # Advantages and use cases of class decorators.		
		
# Decorators for Debugging and Logging	20	
    # Writing decorators for logging function calls.		
    # Profiling function execution time using decorators.		
    # Debugging with decorators: adding print statements.	
	
# Decorators for Authorization and Validation (20 minutes)		
    # Implementing decorators for authentication and authorization.		
    # Validating function inputs using decorators.		
    # Error handling with decorators.		
		
# Decorator Best Practices	10	
    # Best practices for writing clean and maintainable decorators.		
    # Avoiding common pitfalls and issues.		
    # Documentation and testing of decorators.		
		
# Practice and Application	30	
    # Hands-on exercises implementing various decorators.		
    # Applying decorators to real-world scenarios.		
    # Q&A and troubleshooting.		

























# @logging_decorator
# @timeit
# @cacheit
from calendar import c


def fa():
    # task 1
    # heavy calculation
    # task 2
    pass


def v1function(self, a, b):
    return a + b

# @compatibility_check
# @auth_check
def v2function(self, a, b, c):
    return (a + b) * c


# compatibility_check(func)
# if not c:
#     - return func(*args, **kwards, c=1)




# modify or extend the behavior of functions or methods. Decorators are functions themselves that wrap around other functions or methods and provide additional functionality. 
# Code Reusability
# Modularity and Separation of Concerns
# Code Readability and Maintainability
# Dynamism and Flexibility
# Performance Optimization
# Framework and Library Development
# Backward Compatibility






























# USE CASE
# logging, authentication, caching, or error handling to functions or methods without modifying their core logic
# middlewares - authentication (framework)
































def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print(f"\n\n\n")

































def uppercase_decorator(func):
    def wrapper(text):
        result = func(text.upper())
        return result
    return wrapper

def bold_decorator(func):
    def wrapper(text):
        result = "<b>" + func(text) + "</b>"
        return result
    return wrapper


@uppercase_decorator
@bold_decorator
def greet(name):
    return f"Hello, {name}!"

result = greet("Anup")
print(result)
print(f"\n\n\n")

































def repeat(n_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
print(f"\n\n\n")



































class MyDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)
        print("After calling the function")
        return result

@MyDecorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
print(f"\n\n\n")


# Maintaining State
# composition and reuse of functionality across multiple decorators.

def call_counter(func):
    def wrapper(*args, **kwargs):
        count = 0
        count = count + 1
        print(f"Function Decorator :: Function {func.__name__} has been called {count} times")
        return result
    return wrapper


class CallCounter:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Function {self.func.__name__} has been called {self.calls} times")
        return self.func(*args, **kwargs)

@CallCounter
def add(a, b):
    return a + b

# Calling the decorated function multiple times
print(add(1, 2))  # Output: Function add has been called 1 times, 3
print(add(3, 4))  # Output: Function add has been called 2 times, 7
print(add(5, 6))  # Output: Function add has been called 3 times, 11
print(f"\n\n\n")

@call_counter
def add2(a, b):
    return a + b

print(add2(1, 2))
print(add2(1, 2))