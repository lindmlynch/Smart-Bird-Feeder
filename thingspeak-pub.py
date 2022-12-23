#!/usr/bin/python3

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import logging
from dotenv import dotenv_values
# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q=Tralee&units=metric"
CITY = "Tralee"
API_KEY = "5ccfe1a1e84b94d1babd1bb10d85753c"

def kelvin_celsius(kelvin):
	celsius = kelvin - 273.15
	return celsius

# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   temp_celsius = round(kelvin_celsius(temperature),2)
  
   print(f"{CITY:-^30}")
 
   print(f"Celsius: {temp_celsius}")
   
else:
   # showing the error message
   print("Error in the HTTP request")

#load MQTT configuration values from .env file
config = dotenv_values(".env")

#configure Logging
logging.basicConfig(level=logging.INFO)

# Define event callbacks for MQTT
def on_connect(client, userdata, flags, rc):
    logging.info("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    logging.info("Message Sent ID: " + str(mid))

mqttc = mqtt.Client(client_id=config["clientId"])

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# parse mqtt url for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[1:]

# Configure MQTT client with user name and password
mqttc.username_pw_set(config["username"], config["password"])

#Connect to MQTT Broker
mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

#Set Thingspeak Channel to publish to
topic = "channels/"+config["channelId"]+"/publish"

# Publish a message to temp every 15 seconds
while True:
    try:
        temp=round(temp_celsius,2)
        payload="field1="+str(temp)
        mqttc.publish(topic, payload)
        time.sleep(int(config["transmissionInterval"]))
    except:
        logging.info('Interrupted')
