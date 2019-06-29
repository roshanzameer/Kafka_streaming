# Dockerfile

WORKDIR /usr/app

FROM python:3.6

RUN pip install kafka-python
RUN pip install pandas
RUN pip install requests


CMD ["python", "producer.py"]
CMD ["python", "consumer.py"]
