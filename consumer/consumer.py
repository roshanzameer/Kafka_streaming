import json
from kafka import KafkaConsumer
import requests
import pandas as pd
from time import sleep


def consumer_instance(topic_name):
    urls = []

    try:
        print('Connecting to Kafka Topic')
        consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest', bootstrap_servers=['172.17.0.1:9092'],
                                 api_version=(0, 10), consumer_timeout_ms=3000)
        for msg in consumer:
            urls.append((msg.value))
        print('reading from topic closed')
        # sleep(5)
        data_to_csv(urls)


    except Exception as ex:
        print(ex)


def data_to_csv(urls):
    response = []
    for url in list(set(urls)):
        response.append(requests.get(url).json())

    user_data = []
    for data in response:
        for i in data['data']:
            user_data.append(i)

    df = pd.DataFrame(user_data)
    df.to_csv('/tmp/user_data.csv', index=False)

consumer_instance('my_topic')
