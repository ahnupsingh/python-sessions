from timeit import default_timer as timer
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="session-4-task-1.log",
)


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        execution_time = end - start
        print(execution_time)
        if execution_time < 10:
            logging.debug(f"{func.__name__} {execution_time}")
        else:
            logging.error(f"{func.__name__} {execution_time}")

    return wrapper


@calc_time
def sum(a, b):
    sum = 0
    for number in range(a, b):
        sum += number
    return sum


@calc_time
def product(a, b):
    product = 0
    for number in range(a, b):
        product *= number
    return product


sum(0, 200000000)
product(0, 200000000)
