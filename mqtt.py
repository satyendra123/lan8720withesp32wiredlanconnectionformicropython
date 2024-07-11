import paho.mqtt.client as mqtt

class MQTT:
    def __init__(self, client_id, broker, port=1883, topic="default/topic", debug=False):
        self.client = mqtt.Client(client_id)
        self.broker = broker
        self.port = port
        self.topic = topic
        self.debug = debug

    def connect(self):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()
        if self.debug:
            print(f"Connected to MQTT broker {self.broker} on port {self.port}")

    def publish(self, topic, payload):
        self.client.publish(topic, payload)
        if self.debug:
            print(f"Published {payload} to topic {topic}")
