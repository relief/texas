from skimage.measure import structural_similarity as ssim
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
 
	# setup the figure
	#print "MSE: %.2f, SSIM: %.2f\n" % (m, s)
 	return m,s

def equal_images(imageA, imageB):
	m = mse(imageA, imageB)
	if m < 500:
		return True
	return False

def compareSuit(contrast):
	minm = 10000000
	maxs = -2
	minm_suit, maxs_suit = '', ''
	for st in suit:
		m, s = compare_images(suit[st], contrast)
		if m < minm:
			minm = m
			minm_suit = st
		if s > maxs:
			maxs = s
			maxs_suit = st
	if maxs_suit == minm_suit and minm < 10000 and maxs > 0.5:
		return maxs_suit
	return 'unknown'

def compareRank(contrast):
	fittest = -1
	fittest_m = 1000000
	fittest_s = 0
	for i in range(13):
		for hr in range(2):
			m,s = compare_images(rank_img[i][hr], contrast)
			if m < fittest_m:
				fittest_m = m
				fittest_s = s
				fittest = i
	if fittest_m < 4000 and fittest_s > 0.55:
		return str(fittest+1)
	return "unknown"

def compareChupai(contrast):
	return equal_images(state['chupai'], contrast)

def compareRangpai(contrast):
	return equal_images(state['rangpai'], contrast)

state = dict()
state['chupai'] = cv2.cvtColor(cv2.imread("state/chupai.png"), cv2.COLOR_BGR2GRAY)
state['rangpai'] = cv2.cvtColor(cv2.imread("state/rangpai.png"), cv2.COLOR_BGR2GRAY)

suit = dict()
suit['diamonds'] = cv2.cvtColor(cv2.imread("suit/diamond.png"), cv2.COLOR_BGR2GRAY)
suit['clubs'] = cv2.cvtColor(cv2.imread("suit/clubs.png"), cv2.COLOR_BGR2GRAY)
suit['hearts'] = cv2.cvtColor(cv2.imread("suit/heart.png"), cv2.COLOR_BGR2GRAY)
suit['spade'] = cv2.cvtColor(cv2.imread("suit/spade.png"), cv2.COLOR_BGR2GRAY)


rank_img = []
for i in range(1,14):
	h = cv2.cvtColor(cv2.imread("rank/"+str(i)+"h.png"), cv2.COLOR_BGR2GRAY)
	r = cv2.cvtColor(cv2.imread("rank/"+str(i)+"r.png"), cv2.COLOR_BGR2GRAY)
	rank_img.append((h,r))