from kafka import KafkaProducer
import os

def producer_instance():

    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['172.17.0.1:9092'], api_version=(0, 10))
    except Exception as ex:
        print('PRODUCE_URLS', ex)

    finally:
        return _producer

def publish_urls(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message publish successfully')
    except Exception as ex:
        print('publish_urls', ex)

urls = [
    "https://reqres.in/api/users?page=1",
    "https://reqres.in/api/users?page=2",
    "https://reqres.in/api/users?page=3",
    "https://reqres.in/api/users?page=4"
    ]


print('Running Producer..')

kafka_producer = producer_instance()
for url in urls:
    publish_urls(kafka_producer, 'test_dock', 'urls', url)
