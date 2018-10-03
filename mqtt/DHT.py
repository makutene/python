from time import sleep
from umqtt.simple import MQTTClient
import machine

SERVER = 'gualtrapas.ddns.net'  # MQTT Server Address (Change to the IP address of your Pi)
CLIENT_ID = 'asd'

client = MQTTClient(CLIENT_ID,SERVER)  
client.connect()

sensor = machine.ADC(0)

while True:
	h = sensor.read()
	client.publish('soil',str(h))
	sleep(60)
