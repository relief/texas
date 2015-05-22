print '------------Preparing library------------'
import eye
import card
import brain
import time

from dapai import restart, restartJingYing
import random





print '-------------Begin working---------------'
print '----------------Load Eye-----------------'
e = eye.Eye()
print '----------------Load Brain---------------'
b = brain.Brain()

e.saveRecord()	
restart()
my_turn_round = 0
empty_operation = 0

while True:
	print '-----------------------------------------'
	try:
		e.getImage()
	except:
		# time.sleep(1)
		continue
	if e.canChupai() == 0:
		print 'empty_operation: ', empty_operation
		time.sleep(1)
		empty_operation += 1
		if empty_operation == 60:   # 60 * (2+2.5) = 270s = 4.5min
			e.saveRecord()				
			empty_operation = 0
			my_turn_round = 0
			restart()
			time.sleep(3)			
		continue
	own  = e.getOwnCard()
	desk = e.getDesk()
	if len(own) < 2 or len(desk) == 1 or len(desk) == 2:
		continue

	empty_operation = 0
	if desk == []:
		my_turn_round += 1	
	
	canRangpai = e.canRangpai()
	numOfRivals = e.getNumOfRival()
	b.decide(my_turn_round, own, desk, canRangpai, numOfRivals)	
	
	fn = 'all/' + str(random.random()) + '.png'
	e.im.save(fn)
	time.sleep(1*numOfRivals)	
