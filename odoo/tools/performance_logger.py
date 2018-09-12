# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="performance.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


def log_message(action_name, total_time):
    logger.info("PER:%s:%s", action_name, total_time)
