# camera testing script

from datetime import datetime
import picamera



def init():
	camera = PiCamera()
	camera.resolution = (128, 128)
	camera.start_preview()
	# Camera warm-up time

def close_camera():
	camera.stop_preview()
	camera.close()
	

def take_picture():
	filename = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
	camera.capture(filename + '.jpg')
	print('Capture ', filename, 'successfully.')

def take_picture_test():
	camera.capture('test.jpg')