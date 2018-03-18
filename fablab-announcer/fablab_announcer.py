import paho.mqtt.client as mqtt
import time

UPDATE_TIME_IN_SECONDS = 60




client = mqtt.Client()
client.will_set(topic='fablab/status',payload='chiuso', retain=True)
client.connect('iot.eclipse.org',1883)

#Say to world that fablab is open
client.publish(topic='fablab/status',payload='aperto' ,retain=True)

#Update time
now = time.time()
last_time_we_update = now


while True:
    now = time.time()
    if (now - last_time_we_update >= UPDATE_TIME_IN_SECONDS) :
        client.publish(topic='fablab/status',payload='aperto',retain=True)
        last_time_we_update = time.time()
    client.loop(1)
    #This just to slow down updates with ping
    time.sleep(5)
