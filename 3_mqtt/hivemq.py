import time
import paho.mqtt.client as paho
from paho import mqtt
from gpiozero import InputDevice
from time import sleep

hive_mq_cloud = "hivemq broker url"
username = "username"
password = "password"

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("msg id: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# callback for button topic
def btn_callback(client, userdata, msg):
    print("Button pressed: " + str(msg.payload))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)
client.connect(hive_mq_cloud, 8883)

client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

client.subscribe("button", qos=1)
client.message_callback_add("button", btn_callback)

parkingSpot1 = InputDevice(5)
parkingSpot2 = InputDevice(6)

occupiedSpots = {}
prevOccupiedSpots = {}


def updateParkingSpots():
    isOccupied = {}

    isOccupied["spot1"] = not parkingSpot1.is_active
    isOccupied["spot2"] = not parkingSpot2.is_active
    
    return isOccupied


def writeToMQTT(occupiedSpots):
    for spot in occupiedSpots:
        client.publish(f"parking_spots/{spot}", payload=occupiedSpots[spot], qos=1)

client.loop_start()

while True:
    prevOccupiedSpots = occupiedSpots
    occupiedSpots = updateParkingSpots()
    if(occupiedSpots != prevOccupiedSpots):
        writeToMQTT(occupiedSpots)
        print("Parking Spots have Changed " + str(occupiedSpots))
    sleep(1)
