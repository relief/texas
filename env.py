import Image
import ImageComp as ic
import cv2
import numpy

def img2gray(img):
	cv2_data = numpy.array(img) 
	cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

class Env:
	width  = 180
	height = 133
	padding = 21
	left = 500
	next = height + padding
	leftTop = [(left,522),(left,522+next),(left,522+2*next),(left,522+3*next),(left,522+4*next)]
	box_num = (118,2,177,45)
	box_type = (75,5,117,40)
	box_state = (30,780,125,800)
	box_own = (275,955,370,1050)

	def __init__(self):
		self.getImage()

	def getImage(self):
		mode = 'RGBA'
		size = (1080, 1920)
		f = open('data/screenshot.raw', 'rb')
		f.read(12)
		self.im = Image.fromstring(mode, size, f.read())
# im.save('screenshot.png')

	def isChupai(self):
		region_state = self.im.crop(self.box_state)
		return ic.compareChupai(img2gray(region_state))

	def canRangpai(self):
		box = (30,1200,125,1300)
		region_rangpai = self.im.crop(box)
		region_rangpai.save('state/tmp_rangpai.png')
		return ic.compareRangpai()

	def getTypeAndNum(self):
		i = 0
		cards = []
		for lt in self.leftTop:
			i += 1
			box = (lt[0],lt[1],lt[0]+self.width,lt[1]+self.height)
			region = self.im.crop(box)
			#fn = str(random.uniform(0, 100))
			#region.save('deskcard/20150416/'+fn+'.png')

			fn = 'num/tmp_'+str(i)+'.png'
			
			region_num = region.crop(self.box_num)
			region_num.save(fn)
			card_num = ic.compareNum(fn)

			fn = 'type/tmp_'+str(i)+'.png'
			
			region_type = region.crop(self.box_type)
			region_type.save(fn)
			card_type = ic.compareType(fn)
			#print card_num,'_',card_type
			if card_type != "unknown" and card_num != "unknown":
				cards.append(card_type+"_"+card_num)

		return cards

	def getOwnCard(self):
		region_own = self.im.crop(self.box_own)
		import random
		fn = str(random.uniform(0, 100))
		box_card1_suit = (0,12,37,40)
		card1_suit = region_own.crop(box_card1_suit)
		card1_suit.save('own/card1_suit/'+fn+'.png')

		box_card1_rank = (40,6,93,40)
		card1_rank = region_own.crop(box_card1_rank)
		card1_rank.save('own/card1_rank/'+fn+'.png')

		box_card2_suit = (0,50,37,80)
		card2_suit = region_own.crop(box_card2_suit)
		card2_suit.save('own/card2_suit/'+fn+'.png')

		box_card2_rank = (38,57,93,92)
		card2_rank = region_own.crop(box_card2_rank)
		card2_rank.save('own/card2_rank/'+fn+'.png')

		region_own.save('own/all/'+fn+'.png')

