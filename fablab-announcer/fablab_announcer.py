import paho.mqtt.client as mqtt
import time
import json

UPDATE_TIME_IN_SECONDS = 60

#We'll announce various data in json format
data_to_send = {
    'status': 'chiuso' #Fablab Status: OPEN/CLOSED
}

last_will = json.dumps(data_to_send)

client = mqtt.Client()
client.will_set(topic='fablab/announcements',payload=last_will, retain=True)
client.connect('iot.eclipse.org',1883)

#Fablab is open
data_to_send['status'] = 'aperto'

#Say to world that fablab is open
client.publish(topic='fablab/announcements',payload=json.dumps(data_to_send) ,retain=True)

#Update time
now = time.time()
last_time_we_update = now


while True:
    now = time.time()
    if (now - last_time_we_update >= UPDATE_TIME_IN_SECONDS) :
        client.publish(topic='fablab/announcements',payload=json.dumps(data_to_send),retain=True)
        last_time_we_update = time.time()
    client.loop(1)
    #This just to slow down updates with ping
    time.sleep(5)
