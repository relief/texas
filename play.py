from subprocess import call
import env
from dapai import qipai, genzhu, allin, screencap


screencap()
e = env.Env()
#e.im.show()

while True:
	print '-----------------------------------------'
	screencap()
	try:
		e.getImage()
	except:
		continue
	# e.im.save('screen.png')
	#break
	if e.isChupai() == 0:
		continue
	#e.im.save('screen.png')
	print e.getTypeAndNum()
	e.getOwnCard()
	if e.canRangpai():
		genzhu()
	else:
		qipai()

