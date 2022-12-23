from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import datetime
import storeFileFB


pir = MotionSensor(4)
camera = PiCamera()
camera.start_preview()
frame = 1

while True:
	pir.wait_for_motion()
	fileLoc = f'/home/pi/assignment/images/frame{frame}.jpg'
	currentTime = datetime.datetime.now().strftime("%H:%M:%S")
	camera.capture(fileLoc) # capture image and store in fileLoc
	print(f'frame {frame} taken at {currentTime}') # print frame number to console
	storeFileFB.store_file(fileLoc)
	storeFileFB.push_db(fileLoc, currentTime)
	print('Image stored and location pushed to db')
	frame += 1

	pir.wait_for_no_motion()
	camera.stop_preview()
	sleep(30)
	

