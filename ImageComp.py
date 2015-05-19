import numpy as np
import cv2

state = dict()
state['chupai'] = cv2.cvtColor(cv2.imread("state/chupai.png"), cv2.COLOR_BGR2GRAY)
state['rangpai'] = cv2.cvtColor(cv2.imread("state/rangpai.png"), cv2.COLOR_BGR2GRAY)

desk_suit = dict()
desk_suit['diamond'] = cv2.cvtColor(cv2.imread("suit/diamond.png"), cv2.COLOR_BGR2GRAY)
desk_suit['clubs'] = cv2.cvtColor(cv2.imread("suit/club.png"), cv2.COLOR_BGR2GRAY)
desk_suit['heart'] = cv2.cvtColor(cv2.imread("suit/heart.png"), cv2.COLOR_BGR2GRAY)
desk_suit['spade'] = cv2.cvtColor(cv2.imread("suit/spade.png"), cv2.COLOR_BGR2GRAY)

desk_rank = []
for i in range(1,14):
	h = cv2.cvtColor(cv2.imread("rank/"+str(i)+"h.png"), cv2.COLOR_BGR2GRAY)
	r = cv2.cvtColor(cv2.imread("rank/"+str(i)+"r.png"), cv2.COLOR_BGR2GRAY)
	desk_rank.append((h,r))

card1_suit = dict()
card1_suit['diamond'] = cv2.cvtColor(cv2.imread("own/card1_diamond.png"), cv2.COLOR_BGR2GRAY)
card1_suit['club'] = cv2.cvtColor(cv2.imread("own/card1_club.png"), cv2.COLOR_BGR2GRAY)
card1_suit['heart'] = cv2.cvtColor(cv2.imread("own/card1_heart.png"), cv2.COLOR_BGR2GRAY)
card1_suit['spade'] = cv2.cvtColor(cv2.imread("own/card1_spade.png"), cv2.COLOR_BGR2GRAY)

card2_suit = dict()
card2_suit['diamond'] = cv2.cvtColor(cv2.imread("own/card2_diamond.png"), cv2.COLOR_BGR2GRAY)
card2_suit['club'] = cv2.cvtColor(cv2.imread("own/card2_club.png"), cv2.COLOR_BGR2GRAY)
card2_suit['heart'] = cv2.cvtColor(cv2.imread("own/card2_heart.png"), cv2.COLOR_BGR2GRAY)
card2_suit['spade'] = cv2.cvtColor(cv2.imread("own/card2_spade.png"), cv2.COLOR_BGR2GRAY)

card1_rank = []
for i in range(1,14):
	blk = cv2.cvtColor(cv2.imread("own/card1_rank/"+str(i)+"_black.png"), cv2.COLOR_BGR2GRAY)
	red = cv2.cvtColor(cv2.imread("own/card1_rank/"+str(i)+"_red.png"), cv2.COLOR_BGR2GRAY)
	card1_rank.append((blk,red))

card2_rank = []
for i in range(1,14):
	blk = cv2.cvtColor(cv2.imread("own/card2_rank/"+str(i)+"_black.png"), cv2.COLOR_BGR2GRAY)
	red = cv2.cvtColor(cv2.imread("own/card2_rank/"+str(i)+"_red.png"), cv2.COLOR_BGR2GRAY)
	card2_rank.append((blk,red))

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def equal_images(imageA, imageB, threshold):
	m = mse(imageA, imageB)
	if m < threshold:
		return 0
	return m

def compareSuit(contrast):
	for st in desk_suit:
		if equal_images(desk_suit[st], contrast, 1000) == 0:
			return st
	return 'unknown'

def compareCard1Suit(contrast):
	minm, minsuit = 1000000, ''
	for st in card1_suit:
		m = equal_images(card1_suit[st], contrast, 1500)
		if m == 0:
			return st
		if m < minm:
			minm = m
			minsuit = st
	if minsuit == 'spade' and minm < 5500:
		return 'club'
	return 'unknown'

def compareCard2Suit(contrast):
	minm, minsuit = 1000000, ''
	for st in card2_suit:
		m = equal_images(card2_suit[st], contrast, 1500)
		if m == 0:
			return st
		if m < minm:
			minm = m
			minsuit = st
	if minm < 3500:
		return minsuit
	return 'unknown'

def compareRank(contrast):
	minm, mini = 1000000, 0
	for i in range(13):
		for br in range(2):
			m = equal_images(desk_rank[i][br], contrast, 1500)
			if m == 0:	
				return i+1
			if m < minm:
				minm = m
				mini = i
	if minm < 5000:
		return mini+1
	return 'unknown'

def compareCard1Rank(contrast):
	for i in range(13):
		for br in range(2):
			if equal_images(card1_rank[i][br], contrast, 1500) == 0:
				return i+1
	return 'unknown'

def compareCard2Rank(contrast):
	for i in range(13):
		for br in range(2):
			if equal_images(card2_rank[i][br], contrast, 2000) == 0:
				return i+1
	return 'unknown'

def compareChupai(contrast):
	return equal_images(state['chupai'], contrast, 500) == 0

def compareRangpai(contrast):
	return equal_images(state['rangpai'], contrast, 500) == 0

if __name__ == "__main__":
	import os
	path = "own/card2_rank/all/"
	dirs = os.listdir( path )
	import random
	for file in dirs:
		print file
		cimg = cv2.imread(path+file)
		cimg = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
		name = compareCard2Rank(cimg)
		os.rename(path+file, path+str(name)+"_"+str(random.uniform(0, 100))+".png")
