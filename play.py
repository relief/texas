print '------------Preparing library------------'
import env
import card
import brain
import time

from subprocess import call
def screencap():
	cmd = r"adb shell screencap | perl -pe 's/\x0D\x0A/\x0A/g' > data/screenshot.raw;"
	p1 = call(cmd, shell=True)

screencap()
e = env.Env()
b = brain.Brain()
print '-------------Begin working---------------'
my_turn_round = 0
while True:
	print '-----------------------------------------'
	screencap()
	try:
		e.getImage()
	except:
		continue

	if e.canChupai() == 0:
		time.sleep(2)
		continue
	#e.im.save('screen.png')
	own  = e.getOwnCard()
	if len(own) == 0:
		continue
	my_turn_round += 1
	desk = e.getDesk()	
	canRangpai = e.canRangpai()
	b.decide(my_turn_round, own, desk, canRangpai)	
	time.sleep(2)