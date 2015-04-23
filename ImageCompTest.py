# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
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
	m,s = compare_images(diamonds, contrast)
	if m < 1000:
		return "diamonds"
	m,s = compare_images(clubs, contrast)
	if m < 1000:
		return "clubs"
	m,s = compare_images(hearts, contrast)
	if m < 1000:
		return "hearts"
	m,s = compare_images(spade, contrast)
	if m < 1000:
		return "spade"
	return "None"

diamonds = cv2.imread("type/diamond.png")
clubs    = cv2.imread("type/clubs.png")
hearts   = cv2.imread("type/heart.png")
spade	 = cv2.imread("type/spade.png")
diamonds = cv2.cvtColor(diamonds, cv2.COLOR_BGR2GRAY)
clubs = cv2.cvtColor(clubs, cv2.COLOR_BGR2GRAY)
hearts = cv2.cvtColor(hearts, cv2.COLOR_BGR2GRAY)
spade = cv2.cvtColor(spade, cv2.COLOR_BGR2GRAY)

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
		print "best: ", fittest+1," , m = ",fittest_m, "  , s= ",fittest_s
		return str(fittest+1)
	return "unknown"
 	#return str(fittest+1)+"_"+str(fittest_m)+"_"+str(fittest_s)


num_img = []
for i in range(1,14):
	h = cv2.cvtColor(cv2.imread("num/"+str(i)+"h.png"), cv2.COLOR_BGR2GRAY)
	r = cv2.cvtColor(cv2.imread("num/"+str(i)+"r.png"), cv2.COLOR_BGR2GRAY)
	num_img.append((h,r))

#import os
# path = "num/all/"
# dirs = os.listdir( path )
# import random
# for file in dirs:
# 	name = compareNum(path+file)
# 	os.rename(path+file, path+"_"+name+"_"+str(random.uniform(0, 100))+".png")