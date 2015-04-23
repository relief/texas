import Image
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

def compareType(fn="type/tmp.png"):
	global diamonds, clubs, hearts, spade
	contrast = cv2.imread(fn)
	# convert the images to grayscale
	contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

	lm, ls = [], []
	m,s = compare_images(diamonds, contrast)
	lm.append(m)
	ls.append(s)

	m,s = compare_images(clubs, contrast)
	lm.append(m)
	ls.append(s)

	m,s = compare_images(hearts, contrast)
	lm.append(m)
	ls.append(s)

	m,s = compare_images(spade, contrast)
	lm.append(m)
	ls.append(s)	
	
	minm = min(lm)
	maxs = max(ls)
	for i in range(4):
		if lm[i] == minm:
			posm = i
			break
	for i in range(4):
		if ls[i] == maxs:
			poss = i
			break
	#print minm, posm, maxs, poss
	if posm != poss or minm > 10000 or maxs < 0.5:
		return "unknown"
	else:
		if posm == 0:
			return "diamonds"
		elif posm == 1:
			return "clubs"
		elif posm == 2:
			return "hearts"
		else:
			return "spade"

def compareNum(fn="num/tmp.png"):
	contrast = cv2.imread(fn)
	# convert the images to grayscale
	contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
	fittest = -1
	fittest_m = 1000000
	fittest_s = 0
	for i in range(13):
		mh,sh = compare_images(num_img[i][0], contrast)
		mr,sr = compare_images(num_img[i][1], contrast)
		m = min(mh,mr)
		s = max(sh,sr)
		if m < fittest_m:
			fittest_m = m
			fittest_s = s
			fittest = i
	if fittest_m < 4000 and fittest_s > 0.55:
		#print "best: ", fittest+1," , m = ",fittest_m, "  , s= ",fittest_s
		return str(fittest+1)
	return "unknown"

def compareChupai(contrast, fn="state/tmp_chupai.png"):
	global chupai
	m,s = compare_images(chupai, contrast)
	if m < 1000 and s > 0.5:
		return 1
	return 0

def compareRangpai(fn="state/tmp_rangpai.png"):
	global rangpai
	contrast = cv2.imread(fn)
	contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
	m,s = compare_images(rangpai, contrast)
	if m < 3000 and s > 0.5:
		return 1
	return 0

diamonds = cv2.cvtColor(cv2.imread("type/diamond.png"), cv2.COLOR_BGR2GRAY)
clubs = cv2.cvtColor(cv2.imread("type/clubs.png"), cv2.COLOR_BGR2GRAY)
hearts = cv2.cvtColor(cv2.imread("type/heart.png"), cv2.COLOR_BGR2GRAY)
spade = cv2.cvtColor(cv2.imread("type/spade.png"), cv2.COLOR_BGR2GRAY)
chupai = cv2.cvtColor(cv2.imread("state/chupai.png"), cv2.COLOR_BGR2GRAY)
rangpai = cv2.cvtColor(cv2.imread("state/rangpai.png"), cv2.COLOR_BGR2GRAY)

num_img = []
for i in range(1,14):
	h = cv2.cvtColor(cv2.imread("num/"+str(i)+"h.png"), cv2.COLOR_BGR2GRAY)
	r = cv2.cvtColor(cv2.imread("num/"+str(i)+"r.png"), cv2.COLOR_BGR2GRAY)
	num_img.append((h,r))

# import os
# path = "num/all/"
# dirs = os.listdir( path )
# import random
# for file in dirs:
# 	name = compareNum(path+file)
# 	os.rename(path+file, path+"_"+name+"_"+str(random.uniform(0, 100))+".png")