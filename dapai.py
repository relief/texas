from subprocess import call

def qipai():
	cmd = './r qipai > /dev/null'
	p1 = call(cmd, shell=True)
	print 'qipai'

def genzhu():
	cmd = './r genzhu > /dev/null'
	p1 = call(cmd, shell=True)
	print 'genzhu'

def allin():
	cmd = './r allin > /dev/null'
	p1 = call(cmd, shell=True)
	print 'allin'

def screencap():
	cmd = r"adb shell screencap | perl -pe 's/\x0D\x0A/\x0A/g' > data/screenshot.raw;"
	p1 = call(cmd, shell=True)