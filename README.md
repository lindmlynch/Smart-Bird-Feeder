# smart-bird-feeder
I was curious to know more about the feeding habit of birds so I created a smart bird feeder. 
This was achieved by attaching a RPi, camera and PIR sensor, in a weather proof casing, to a bird feeding station in the garden. Then running a python script that would capture an image at intervals when motion is detected.
The OpenWeather API was used to gather weather information in the area and then triggering a react on ThingSpeak to send a reminder tweet to feed the birds when the temperature goes below 5C.
ThingSpeak was used to gather data on how often motion was detected at the bird feeder.
https://thingspeak.com/channels/1982377
Images captured were stored on a Firebase database.
Glitch sites to notify of activity at the feeder and to show findings.
