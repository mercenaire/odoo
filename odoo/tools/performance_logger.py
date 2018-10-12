# importing module
import logging
from kafka import KafkaProducer
import re
import time
from odoo.tools.kafka_config import KAFKA_CONN,KAFKA_TEST_TOPIC
from odoo.so_result_pb2 import SalesResultModel

# Create and configure logger
import threading

logging.basicConfig(filename="performance.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

producer = KafkaProducer(bootstrap_servers=[KAFKA_CONN], api_version=(0, 10, 1))

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
                genertae_cron_result('Completed', 0, 0, 0, [0], test_id,
                                     message)
            except Exception as e:
                message = "Something went wrong when processing the test results for Test Id {0} \n" \
                          "More Information {1}".format(test_id, e)
            # producer.send('test_completed', message.encode())
                genertae_cron_result('failed', 0, 0, 0, [0], test_id,message)

def genertae_cron_result(type, so_id, so_line_ids, pt_id, ptl_ids, test_id, msg):
    so_res_model = SalesResultModel()
    so_res_model.so_details.id = so_id
    so_res_model.so_details.name = "SO" + str(so_id)
    so_res_model.so_details.sol_line_ids.append(so_line_ids)
    so_res_model.pt_details.id = pt_id
    so_res_model.pt_details.name = " Arisan Payment,  SO" + str(so_id)
    so_res_model.pt_details.ptl_line_ids.extend(ptl_ids)
    so_res_model.type = type
    so_res_model.message = msg
    so_res_model.test_id = test_id
    res = so_res_model.SerializeToString()
    send_message_kafka(res)

def send_message_kafka(message):
    try:
        print(producer)
        producer.send(KAFKA_TEST_TOPIC, message).get(timeout=30)
        producer.flush()
    except Exception as e:
        print(e)





