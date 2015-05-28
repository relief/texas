import Image
import os
import cv2
import numpy
import random


def img2gray(img):
	cv2_data = numpy.array(img)
	cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

def flucInLine(A):
	threshold = 110
	change = 0
	for i in range(len(A)):
		if A[i] > threshold and A[i-1] <= threshold:
			change += 1
	return change

def detectDigit(im):
	col, row = im.size
	pixels = img2gray(im)

	feature = ''
	feature+=str(flucInLine(pixels[:,col/5]))
	feature+=str(flucInLine(pixels[:,col/5*2]))
	feature+=str(flucInLine(pixels[:,col/5*3]))
	feature+=str(flucInLine(pixels[:,col/5*4]))
	feature+=str(flucInLine(pixels[row/5,:]))
	feature+=str(flucInLine(pixels[row/5*2,:]))
	feature+=str(flucInLine(pixels[row/5*4,:]))
	feature+=str(flucInLine(pixels[row/5*5,:]))
	mapToNum = {
		'22221221': 0,
		'11111100': 1,
		'11122232': 2,
		'21122232': 3,
		'21122332': 3,
		'12211211': 4,
		'21212332': 5,
		'21222332': 5,
		'22211331': 6,
		'11111221': 7,
		'22222332': 8,
		'12221331': 9,
		'11221331': 9,
		'00000000': 'end',
		'11112223': 'wan',
		'00000111': '.',
	}
	if feature in mapToNum:
		label = mapToNum[feature]
	else:
		label = "Unknown"
	return label

def getPotWan(im):
	pot = ''
	dotline = 9
	# im.show()	
	b = (0,0,33,width)
	img = im.crop(b)
	pot += str(detectDigit(img))
	# img.show()
	b = (0,width,33,dotline+width)
	# print b
	img1 = im.crop(b)
	# img1.show()
	pot += str(detectDigit(img1))
	numAfterDot = 0
	for h in range(width+dotline, 81, width):
		b = (0,h,33,h+width)
		img = im.crop(b)
		# img.show()
		label = detectDigit(img)	
		if label == 'wan':
			# print float(pot) * 10000
			return int(float(pot) * 10000)
		pot += str(label)
	return -1

def getPot(im):
	pot = 0
	# im.show()
	for h in range(padding, 81, width):
		b = (0,h,33,h+width)
		img = im.crop(b)
		label = detectDigit(img)	
		if label == 'end':
			return pot
		elif label == 'Unknown':
			return getPotWan(im)
		else:
			pot = pot * 10 + label
	return pot

padding = 0
width = 19

if __name__ == '__main__':
	path = "pot/all/"
	dirs = os.listdir( path )

	for file in dirs:	
		if file[-1] != 'g':
			continue
		print file
		im = Image.open(path+file)
		pot = getPot(im)
		print pot
		im.save('pot/pot/'+str(pot)+'_'+str(random.random())+'.png')