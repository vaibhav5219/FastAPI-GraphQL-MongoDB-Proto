from confluent_kafka import Consumer, KafkaError

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'consumer-group-1',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)

consumer.subscribe(['orders'])
print("Consumer is listening / subscribed to the 'orders' topic...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages with a timeout of 1 second

        if msg is None:
            continue  # No message received, continue polling
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"End of partition reached {msg.topic()} [{msg.partition()}]")
            else:
                print(f"X Error occurred: {msg.error().str()}")
            continue

        # Process the received message
        value = msg.value().decode('utf-8')
        topic = msg.topic()
        offset = msg.offset()
        print(f"Received message: {value} from topic {topic} at offset {offset}")

except KeyboardInterrupt:
    print("Consumer is shutting down...")

finally:
    consumer.close()
