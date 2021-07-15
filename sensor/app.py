import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker ="localhost" 

client = mqtt.Client("testttt")
client.connect(mqttBroker, 1883) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("temperature/test", randNumber)
    print("Just published " + str(randNumber) + " to topic temperature/test")
    time.sleep(1)