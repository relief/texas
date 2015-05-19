import Image
import ImageComp as ic
import cv2
import numpy
import card

def img2gray(img):
	cv2_data = numpy.array(img) 
	cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

class Eye:
	width  = 180
	height = 133
	padding = 21
	left = 500
	next = height + padding
	leftTop = [(left,522),(left,522+next),(left,522+2*next),(left,522+3*next),(left,522+4*next)]
	box_rank = (118,2,177,45)
	box_suit = (75,5,117,40)
	box_own = (275,955,370,1050)

	def __init__(self):
		self.getImage()

	def getImage(self):
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
		i = 0
		cards = []
		for lt in self.leftTop:
			i += 1
			box = (lt[0],lt[1],lt[0]+self.width,lt[1]+self.height)
			region = self.im.crop(box)
			
			region_rank = region.crop(self.box_rank)
			card_rank = ic.compareRank(img2gray(region_rank))
			
			region_suit = region.crop(self.box_suit)
			card_suit = ic.compareSuit(img2gray(region_suit))
			#print card_rank,'_',card_suit
			if card_suit != "unknown" and card_rank != "unknown":
				cards.append(card.Card(card_suit, card_rank))
				#cards.append(card_suit+"_"+str(card_rank))
			else:
				return cards
		return cards

	def getOwnCard(self):
		region_own = self.im.crop(self.box_own)
		import random
		fn = str(random.uniform(0, 100))

		box_card1_suit = (0,12,37,40)
		card1_suit = ic.compareCard1Suit(img2gray(region_own.crop(box_card1_suit)))

		box_card1_rank = (40,6,93,40)
		card1_rank = ic.compareCard1Rank(img2gray(region_own.crop(box_card1_rank)))
		
		#card1_rank.save('own/card1_rank/'+fn+'.png')

		box_card2_suit = (0,50,37,80)
		card2_suit = ic.compareCard2Suit(img2gray(region_own.crop(box_card2_suit)))
		# card2_suit = region_own.crop(box_card2_suit)
		# card2_suit.save('own/card2_suit/'+fn+'.png')

		box_card2_rank = (38,57,93,92)
		card2_rank = ic.compareCard2Rank(img2gray(region_own.crop(box_card2_rank)))

		#region_own.save('own/all/'+fn+'.png')
		own_cards = []
		#print card1_suit+"_"+str(card1_rank),card2_suit+"_"+str(card2_rank)
		if card1_suit != "unknown" and card1_rank != "unknown" and card2_suit != "unknown" and card2_rank != "unknown":
				own_cards.append(card.Card(card1_suit, card1_rank))			
				own_cards.append(card.Card(card2_suit, card2_rank))	
				#own_cards.append(card1_suit+"_"+str(card1_rank))
				#own_cards.append(card2_suit+"_"+str(card2_rank))
		return own_cards
