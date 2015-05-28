import Image
import os
import cv2
import numpy
import random

threshold = 180
Geng_height = 46
def img2gray(img):
	cv2_data = numpy.array(img)
	cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

def flucInLine(A):
	threshold = 180
	change = 0
	cnt = 0
	for i in range(len(A)):
		if A[i] > threshold:
			cnt += 1
			if cnt >= 3:
				change += 1
				cnt = 0
		else:
			cnt = 0
	return change

def firstWhite(A):
	i = 0
	for ele in A:
		if ele > threshold:
			return i
		i += 1
	return i

def detectDigit(A):
	row, col = A.shape
	# print row, col
	# print A
	feature = ''
	feature+=str(flucInLine(A[:,col/2]))
	feature+=str(flucInLine(A[row/2,:]))
	# feature+=str(flucInLine(A[row-1,:]))

	mapToNum = {
		'22222414': 0,
		'22223514': 0,
		'22223314': 0,
		'22222314': 0,
		'11112271': 1,
		'11112261': 1,
		'11111221': 1,
		'11113133': 2,
		'11113233': 2,
		'11113134': 2,
		'12123225': 3,
		'12123224': 3,
		'12211121': 4,
		'22211121': 4,
		'11121422': 5,
		'11121423': 5,
		'23122422': 6,
		'24123414': 6,
		'11111022': 7,
		'11111021': 7,
		'11111011': 7,
		'11111111': 'dot',
	}
	print feature
	return feature
	if feature in mapToNum:
		label = mapToNum[feature]
	else:
		label = -1
	return label

def getNum(im):
	# im.show()
	col, row = im.size
	pixels = img2gray(im)
	# print col, row
	whiteFaced = False
	last_h = 0
	cnt = 0
	val = ''
	# im.show()
	for h in range(row):
		left = firstWhite(pixels[h,:])
		print left, col
		if left < col:
			if not whiteFaced:
				whiteFaced = True
				last_h = h
				continue
		else:
			if whiteFaced:
				whiteFaced = False
				if h - last_h < 4:
					continue
				for l in range(col):
					pix = pixels[last_h:h-1,l]
					if firstWhite(pix) < h - last_h - 1:
						break	
				for r in range(col-1, -1, -1):
					pix = pixels[last_h:h-1,r]
					if firstWhite(pix) < h - last_h - 1:
						break		
				b = (l, last_h, r, h - 1)
				# im.crop(b).show()

				# d = detectDigit(pixels[last_h:h-1,l:r])
				im.crop(b).save('money/digit/'+str(random.random())+'.png')
				# if detectDigit(pixels[last_h:h-1,l:r]) < 0:
				# 	return 1000000
				
				# if d == 'wan':
				# 	return int(float(val) * 10000)
				# elif d == 'dot':
				# 	val += '.'
				# else:
				# 	val += str(d)
	return 1

def getState(im):
	col, row = im.size
	pixels = img2gray(im)
	# detectDigit(pixels)
	# im.show()
	# return 
	label = getNum(im)
	
	if isinstance(label, int) and label < 0:
		label = 'unknown'
	return label

def main():
	path = "money/digit/"
	dirs = os.listdir( path )
	width = 44
	height= 149
	box = (161,822,161+width,822+height)
	low = 1

	padding = 0
	width = 19
	for file in dirs:	
		if file[-1] != 'g':
			continue
		# if random.random() < 0.9:
			# continue
		print file
		im = Image.open(path+file)
		# getNum(im)

		# continue
		d = detectDigit(img2gray(im))
		# if d < 0:
		# 	im.show()
		# 	break
		# else:
		os.rename(path+file, path+str(d)+"_"+str(random.random())+".png")
		# except:
		# 	os.rename(path+file, path+"error_"+str(random.random())+".png")
		# im.save('money/all/'+str(random.random())+'.png')
# 
if __name__ == '__main__':
	main()

To-do:
	go back to image compare