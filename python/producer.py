from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    # bootstrap_servers=['34.125.153.160:9092'],
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
for j in range(9999):
    print("Iteration", j)
    data = {'counter': j}
    producer.send('percobaan', value=data)
    sleep(3)