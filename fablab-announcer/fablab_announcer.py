import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.will_set(topic='fablab/status',payload='closed')
client.username_pw_set('MQTT_USERNAME','MQTT_PASSWORD')
client.connect('m23.cloudmqtt.com',19543)


while True:
    client.publish(topic='fablab/status',payload='open',retain=True)
    time.sleep(60)
