import json
from kafka import KafkaConsumer
import requests
import pandas as pd
from time import sleep


def consumer_instance(topic_name):
    urls = []
    try:
        consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest', bootstrap_servers=['kafka:9092'],
                             api_version=(0,10), consumer_timeout_ms=3000)
        for msg in consumer:
            urls.append((msg.value))
        consumer.close()
        sleep(5)
        data_to_csv(urls)
        
    except Exception as ex:
        print(ex)

def data_to_csv(urls):

    response = []
    for url in urls:
        response.append(json.loads(requests.get(url).content.decode('utf-8')))

    user_data = []
    for data in response:
        for i in data['data']:
            user_data.append(i)

    df = pd.DataFrame(user_data)
    df.to_csv('user_data.csv', index=False)


consumer_instance('zylotech')
