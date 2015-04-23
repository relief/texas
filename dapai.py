from subprocess import call

def qipai():
	cmd = './r qipai > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: qipai'

def genzhu():
	cmd = './r genzhu > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: genzhu'

def allin():
	cmd = './r allin > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: allin'

def addone():
	cmd = './r allone > /dev/null'
	p1 = call(cmd, shell=True)
	print 'Decision: addone'

