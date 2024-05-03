# DEBUGGING

# print statements
# logging
# pdb


# looking at code done by others
# try to modify / add a new feature
# try to find out and eliminate bug if any
# refactor the code
# Test cases



































import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='session-1.log',
    # filemode='w'
)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("Division by zero occurred")
    else:
        logging.info(f"Division result: {result}")

# Example usage
divide(10, 2)
divide(10, 0)


# Log levels - INFO, DEBUG, ERROR
# Log message format
# Log files
# Log mode (filemode)














# pdb
import pdb

def natural_sum(num, sum=0) -> int:
    sum = sum + num
    pdb.set_trace()
        
    if num == 0:
        return sum
    else:
        return natural_sum(num-1, sum)


print(natural_sum(5))


# Setting a breakpoint using pdb
# pdb commands - n, s, c, p, q
