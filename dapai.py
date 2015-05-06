from subprocess import call

def qipai():
	cmd = './r qipai > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: qipai'

def genzhu():
	cmd = './r genzhu > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: genzhu'

def rangpai():
	cmd = './r genzhu > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: rangpai'

def allin():
	cmd = './r allin > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: allin'

def addone():
	cmd = './r addone > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: addone'

def restart():
	# cmd = './r restart > /dev/null'
	cmd = './r restart > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Restart!'

def restartPuTong():
	# cmd = './r restart > /dev/null'
	cmd = './r restartPuTong > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Restart!PuTong'

def restartJingYing():
	cmd = './r restartJingYing > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Restart!JingYing'