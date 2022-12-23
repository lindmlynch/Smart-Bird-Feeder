#!/usr/bin/python3

from urllib.request import urlopen
import json
import time
from gpiozero import MotionSensor
from dotenv import dotenv_values

#load configuration values from .env file
config = dotenv_values(".env")
baseURL="https://api.thingspeak.com/update?api_key=" + config["apiWriteKey"]

interval = int(config["transmissionInterval"])

def writeData(motion):
	print(baseURL + "&field2=" +str(motion))
	conn = urlopen(baseURL + "&field2=" +str(motion))
	print(conn.read())
	conn.close()

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("Motion Detected")
	motion=1
	writeData(motion)
	time.sleep(interval)
