from confluent_kafka import Producer
import uuid
import json

producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'producer-1'
}

producer = Producer(producer_config)


order = {
    "order_id": str(uuid.uuid4()),
    "user" : "John Doe",
    "product": "Laptop",
    "item" : "Super Fast Laptop",
    "price": 1999.99,
    "quantity": 1
}

order_json = json.dumps(order).encode('utf-8')
producer.produce(
    topic='orders',
    value=order_json,
    callback=lambda err, msg: print(f"Message sent to topic {msg.topic()} with value {msg.value().decode('utf-8')} msg-offset: {msg.offset()} \
  msg-partition: {msg.partition()}")   
)
producer.flush()


# To run the kafka with docker on local -
# docker compose up -d --build

# To run the producer -
# python producer.py

# To check the topics in kafka -
# docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
# docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092 --describe --topic orders
## To display the messages from the topic -
# docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning