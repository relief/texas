import Image
import ImageComp as ic
import cv2
import numpy
import card
from subprocess import call
import datetime
import random

def img2gray(img):
	cv2_data = numpy.array(img) 
	cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

class Eye:
	def __init__(self):
		self.getImage()

	def screencap(self):
		cmd = r"adb shell screencap | perl -pe 's/\x0D\x0A/\x0A/g' > data/screenshot.raw;"
		p1 = call(cmd, shell=True)

	def saveRecord(self):
		box = (800,230,1300,650)
		fn = 'record/' + str(datetime.datetime.now())[:-7] + '.png'
		self.im.rotate(90).crop(box).save(fn)

	def getImage(self):
		self.screencap()
		mode = 'RGBA'
		size = (1080, 1920)
		f = open('data/screenshot.raw', 'rb')
		f.read(12)
		self.im = Image.fromstring(mode, size, f.read())

	def canChupai(self):
		box = (30,780,125,800)
		region_state = self.im.crop(box)
		return ic.compareChupai(img2gray(region_state))

	def canRangpai(self):
		box = (30,1200,125,1300)
		region_rangpai = self.im.crop(box)
		return ic.compareRangpai(img2gray(region_rangpai))

	def getDesk(self):
		height = 180
		width  = 133
		padding= 21
		box_rank = (118,2,177,45)
		box_suit = (75,5,117,40)
		left = 500
		next = width + padding
		leftTop = [(left,522),(left,522+next),(left,522+2*next),(left,522+3*next),(left,522+4*next)]

		cards = []
		for lt in leftTop:
			box = (lt[0],lt[1],lt[0]+height,lt[1]+width)
			region = self.im.crop(box)
			
			region_rank = region.crop(box_rank)
			card_rank = ic.compareRank(img2gray(region_rank))
			
			region_suit = region.crop(box_suit)
			card_suit = ic.compareSuit(img2gray(region_suit))
			
			if card_suit != "unknown" and card_rank != "unknown":
				cards.append(card.Card(card_suit, card_rank))
			else:
				return cards
		return cards

	def getOwnCard(self):
		box_own = (275,955,370,1050)
		region_own = self.im.crop(box_own)

		box_card1_suit = (0,12,37,40)
		card1_suit = ic.compareCard1Suit(img2gray(region_own.crop(box_card1_suit)))

		box_card1_rank = (40,6,93,40)
		card1_rank = ic.compareCard1Rank(img2gray(region_own.crop(box_card1_rank)))

		box_card2_suit = (0,50,37,80)
		card2_suit = ic.compareCard2Suit(img2gray(region_own.crop(box_card2_suit)))

		box_card2_rank = (38,57,93,92)
		card2_rank = ic.compareCard2Rank(img2gray(region_own.crop(box_card2_rank)))

		own_cards = []
		if card1_suit != "unknown" and card1_rank != "unknown" and card2_suit != "unknown" and card2_rank != "unknown":
				own_cards.append(card.Card(card1_suit, card1_rank))			
				own_cards.append(card.Card(card2_suit, card2_rank))	
		return own_cards

	def getPot(self):
		box = (787, 880, 822, 980)
		return 1

	def getNumOfRival(self):
		width = 40
		height= 10
		box = [(214,339,214+width,339+height),(220,1488,220+width,1488+height),(400, 46, 400+width, 46+height),(410,1747,410+width,1747+height),(734,94,734+width,94+height),(738,1711,738+width,1711+height),(842,377,842+width,377+height),(853,1410,853+width,1410+height)]
		numOfRivals = 0
		for b in box:
			img = self.im.crop(b)
			s =  numpy.sum(img)
			if s > 260000 and s < 300000:
				numOfRivals += 1
		return numOfRivals



