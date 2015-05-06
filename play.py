print '------------Preparing library------------'
import env
import card
import brain
import time
import datetime
from dapai import restart, restartJingYing

from subprocess import call

def screencap():
	cmd = r"adb shell screencap | perl -pe 's/\x0D\x0A/\x0A/g' > data/screenshot.raw;"
	p1 = call(cmd, shell=True)


screencap()
e = env.Env()
b = brain.Brain()
print '-------------Begin working---------------'
my_turn_round = 0
empty_operation = 0

# restartJingYing()		
# fn = 'record/' + str(datetime.datetime.now())[:-7] + '.png'
# e.im.rotate(90).crop((800,230,1300,650)).save(fn)

while True:
	print '-----------------------------------------'
	screencap()
	try:
		e.getImage()
		if e.canChupai() == 0:
			print 'empty_operation: ', empty_operation
			time.sleep(min(10/(my_turn_round+1),2))
			empty_operation += 1
			if empty_operation == 60:   # 60 * (2+2.5) = 270s = 4.5min
				fn = 'record/' + str(datetime.datetime.now())[:-7] + '.png'
				e.im.rotate(90).crop((800,230,1300,650)).save(fn)
				empty_operation = 0
				my_turn_round = 0
				restart()
				time.sleep(5)			
			continue
		own  = e.getOwnCard()
		if len(own) < 2:
			continue
		empty_operation = 0
		desk = e.getDesk()
		if desk == []:
			my_turn_round += 1	
		
		canRangpai = e.canRangpai()
		b.decide(my_turn_round, own, desk, canRangpai)	
		time.sleep(3)
	except:
		continue
	
