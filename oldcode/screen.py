from subprocess import Popen, PIPE, check_output
import Image
import ImageComp as ic


def getScreenshot():
	screencap_raw = open('data/screenshot.raw', 'w')
	s = ''
	cmd1 = "adb shell screencap"
	cmd2 = "perl -pe 's\/\\\\x0D\\\\x0A\/\\\\x0A\/g'"
	print cmd1.split(' ')
	print cmd2.split(' ')
	p1 = Popen(cmd1.split(' '), stdout=PIPE)
	
	#p2 = Popen(cmd2.split(' '), stdin=p1.stdout, stdout=screencap_raw)
	#output = p2.communicate()[0] #run our commands
	#screencap_raw.close()
	import Image
	mode = 'RGBA'
	size = (1080, 1920)
	f = open('data/screenshot.raw', 'rb')
	im = Image.frombuffer(mode, size, p1.stdout.read(), "raw", mode, 0, 1)
	im.show()

	import sys
	import cv2
	import numpy

	stdin = sys.stdin.read()
	array = numpy.frombuffer(stdin, dtype='uint8')
	img = cv2.imdecode(array, 1)
	cv2.imshow("window", img)

def getScreenshot1():
	cmd1 = "adb shell screencap"
	cmd2 = "perl -pe 's/\x0D\x0A/\x0A/g'"
	print cmd1.split(' ')
	print cmd2.split(' ')
	s = check_output(cmd1.split(' '))
	import cv2
	import numpy

	array = numpy.frombuffer(s, dtype='uint8')
	img = cv2.imdecode(array, 1)
	cv2.imshow("window", img)
	cv2.waitKey()
