# importing module
import logging
from kafka import KafkaProducer
import re
import time
from odoo.tools.kafka_config import KAFKA_CONN,KAFKA_TEST_TOPIC

# Create and configure logger
import threading

logging.basicConfig(filename="performance.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

producer = KafkaProducer(bootstrap_servers=[KAFKA_CONN])

# def log_message(action_name, total_time):
#     if hasattr(threading.current_thread(), 'test_id'):
#         logger.info("%s:PER:%s:%s", threading.current_thread().test_id, action_name, total_time)

def log_message(action_name, total_time):
    if hasattr(threading.current_thread(), 'test_id'):
        logger.info("PER:%s:%s:%s", threading.current_thread().test_id, '3', total_time)

def log_message_kafka(action_name, total_time, test_id, is_done):
        logger.info("PER:%s:%s:%s", test_id, action_name, total_time)
        if is_done:
            try:
                time.sleep(6)
                no_request = decode_time = execute_db = prepare_db = 0
                f = open("performance.log", "r")
                log_content = f.read()
                f.close()
                pattern = re.compile(r'PER+:' + str(test_id) + '+:(\d)' + '+:(\d*)')
                matches = re.findall(pattern, log_content)
                for match in matches:
                    action_type = int(match[0])
                    if action_type == 1:
                        decode_time += int(match[1])
                    elif action_type == 2:
                        no_request += 1
                        prepare_db += int(match[1])
                    elif  action_type == 3:
                        execute_db += int(match[1])
                total_time_millis = ((decode_time + prepare_db +  execute_db) / 1000)
                message = "Results for Test Id :  {0} \n" \
                          "Decode protobuf :   {2} ms \n" \
                          "Prepare DB Call :   {3} ms \n" \
                          "Execute DB Call :   {4} ms \n" \
                          "Total Time :   {1} ms \n" \
                          "Total Request :  {5} \n" \
                          "TPS : {6} ms".format(test_id, total_time_millis, (decode_time / 1000) , (prepare_db / 1000 ) , execute_db / 1000, no_request, total_time_millis/ no_request)
            except Exception as e:
                message = "Something went wrong when processing the test results for Test Id {0} \n" \
                          "More Information {1}".format(test_id, e)
            # producer.send('test_completed', message.encode())
            producer.send(KAFKA_TEST_TOPIC,  message.encode())





