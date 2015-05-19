from dapai import qipai, genzhu, allin, addone, rangpai
import twoCards
import hand
import card
import random

class Brain:
	def __init__(self):
		self.twoC = twoCards.TwoCards()

	def print_current(self, game_round, own, desk, canRangpai):
		print "My turn: ", game_round
		print "Own: ",
		for o in own:
			print o,
		print "\nDesk: ",
		for d in desk:
			print d,
		print "\ncanRangpai: ", canRangpai

	def decide(self, game_round, own=[], desk=[], canRangpai=False):
		self.print_current(game_round, own, desk, canRangpai)
		print 'Reasons:'
		numDesk = len(desk)
		if numDesk == 0:
			winRate = self.twoC.getRate(own[0], own[1], game_round)
		else:
			besthand = self.getMaxHand(own, desk)
			print '	Hand: ', besthand.handtype
			winRate = self.getWinRate(own, desk, besthand)
		self.decideOnRate(winRate, game_round, canRangpai, numDesk)
	 
	def getMaxHand(self, own, desk):
		maxhand = None
		cards = own + desk

		numCards = len(cards)
		for c0 in range(numCards-4):
			for c1 in range(c0+1, numCards-3): 
				for c2 in range(c1+1, numCards-2):
					for c3 in range(c2+1, numCards-1): 
						for c4 in range(c3+1, numCards):
							h = hand.Hand(cards[c0], cards[c1], cards[c2], cards[c3], cards[c4])
							if maxhand == None or h >= maxhand:
								maxhand = h
		return maxhand		

	def getWinRate(self, own, desk, besthand):
		total = 0
		win = 0
		for s1 in ['diamond','club','heart','spade']:
			for r1 in range(1, 14):
				c1 = card.Card(s1, r1)
				if c1 in own or c1 in desk:
					continue
				for s2 in ['diamond','club','heart','spade']:
					for r2 in range(1, 14):
						c2 = card.Card(s2, r2)
						if c2 in own or c2 in desk or c2 == c1:
							continue
						total += 1
						bestcomp = self.getMaxHand([c1,c2], desk)
						if besthand >= bestcomp:
							win += 1
		return win*100/total

	def decideOnRate(self, prob, game_round, canRangpai, numDesk):
		
		threshold = 81 - game_round
		if numDesk > 0:
			threshold += numDesk * 3
		print "	prob: ",prob, ' ,threshold: ', threshold
		rand = random.random()
		if prob > threshold:
			if prob - threshold > 20:
				if rand > 0.5:
					allin()
				else:
					addone()
			elif prob - threshold > 10:
				if  rand > 0.9:
					allin()
				elif rand > 0.5:
					addone()
			else:
				if rand > 0.7:
					addone()
			genzhu()   # Sometimes you can not addone or allin... then, 
		elif canRangpai:
			rangpai()
		else:
			qipai()