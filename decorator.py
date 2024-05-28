# Implement a decorator that profiles any function execution time.
# print and write to log file as well
# ex:
#     2024-05-12 14:58:45,788 - DEBUG - {func_name} {execution_time}
#     2024-05-12 14:58:45,788 - ERROR - {func_name} {execution_time > 10s}
import logging
import time
import pdb

logging.basicConfig(
    filename="logfile.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


def calc(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        pdb.set_trace()
        execution_time = end_time - start_time
        if execution_time > 10:
            logging.error(f"{func.__name__} {execution_time:.2f} > 10s")
        else:
            logging.debug(f"{func.__name__} {execution_time:.2f}")
        print(f"{func.__name__} {execution_time:.2f}")
        return result

    return wrapper


@calc
def add(a, b):
    return a + b


@calc
def multiply(a, b):
    time.sleep(15)
    return a * b


add(1, 2)
multiply(3, 4)
