# importing module
import logging

# Create and configure logger
import threading

logging.basicConfig(filename="performance.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


def log_message(action_name, total_time):
    if hasattr(threading.current_thread(), 'test_id'):
        logger.info("%s:PER:%s:%s", threading.current_thread().test_id, action_name, total_time)
