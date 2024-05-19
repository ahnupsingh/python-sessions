from datetime import datetime
import logging

logging.basicConfig(
    filename='logs/time-log.log', 
    filemode='a', 
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
    )
logger = logging.getLogger(__name__)


def log_time(func: callable) -> callable:
    """Decorator that logs the amount of time required to execute a function to time-log.log file """

    def wrapper(*args, **kwargs) -> None:
        """ Helper wrapper function for log_time decorator """
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        total_time_taken = end_time - start_time
        print(f"Total Time Taken: {total_time_taken}")
        # import pdb
        # pdb.set_trace()
        total_time_taken = total_time_taken.total_seconds()
        if total_time_taken > float(10.0):
            logging.error(f"Time Taken to Execute {func.__name__} is {total_time_taken} Seconds")
        else:
            logging.info(f"Time Taken to Execute {func.__name__} is {total_time_taken} Seconds")
    return wrapper

@log_time
def squares_upto(upper_range: int) -> list:
    """ A function that takes a upper_range as input and returns a list of squared of each number upto that upper_range"""
    numbers = [number**2 for number in range(upper_range)]
    import time
    time.sleep(10)
    return numbers

square_numbers_list = squares_upto(1000000)




