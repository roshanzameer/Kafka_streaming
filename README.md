A containerized python service to convert JSON reponse of a webpage to CSV using Pandas and Kafka for streaming URLs to the consumer where transformation takes place.

1. The 'Pythonised' Kafka plugin offered by the package Kafka-python has been invoked. 
2. The Producer module streams the URLs to a predefined Topic.
3. The Consumer module reads the byte-stream from the Topic, iterates over the data and builds a Pandas DataFrame which is then exported to a CSV file.
