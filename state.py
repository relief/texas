import Image
import os
import cv2
import numpy
import random

threshold = 127
Geng_height = 46
def img2gray(img):
	cv2_data = numpy.array(img)
	cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

def flucInLine(A):
	change = 0
	cnt = 0
	for i in range(len(A)):
		if A[i] > threshold:
			cnt += 1
			if i == 0 or A[i-1] <= threshold or cnt >= 10:
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
	feature = ''
	feature+=str(flucInLine(A[:,col/4]))
	feature+=str(flucInLine(A[:,col/2]))
	feature+=str(flucInLine(A[:,col/4*3]))
	feature+=str(flucInLine(A[:,1]))
	feature+=str(flucInLine(A[:,col-1]))
	feature+=str(flucInLine(A[1,:]))
	feature+=str(flucInLine(A[row/2,:]))
	feature+=str(flucInLine(A[row-1,:]))

	mapToNum = {
		'22222322': 0,
		'22222323': 0,
		'22222223': 0,
		'11131241': 1,
		'11132241': 1,
		'11132133': 2,
		'11132233': 2,
		'11132332': 2,
		'22122133': 3,
		'22122132': 3,
		'32211131': 4,
		'32211121': 4,
		'13123333': 5,
		'13123135': 5,
		'13123133': 5,
		'13123331': 5,
		'23122232': 6,
		'23122332': 6,
		'11113131': 7,
		'11113141': 7,
		'22222332': 8,
		'22222333': 8,
		'13222532': 9,
		'13222232': 9,
		'11111111': 'dot',
		'22135231': 'wan',
	}
	if feature in mapToNum:
		label = mapToNum[feature]
	else:
		# print feature
		label = 'u_'+feature+'_'
	return label

def getNum(im):
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
				for r in range(col, -1, -1):
					pix = pixels[last_h:h-1,r]
					if firstWhite(pix) < h - last_h - 1:
						break		
				# if detectDigit(pixels[last_h:h-1,l:r]) < 0:
				# 	b = (l, last_h, r, h - 1)
				# 	# im.crop(b).show()
				# 	# exit()
				# 	return 1000000
				d = detectDigit(pixels[last_h:h-1,l:r])
				if d == 'wan':
					return int(float(val) * 10000)
				elif d == 'dot':
					val += '.'
				elif isinstance(d,str) and d[0] == 'u':
					b = (l, last_h, r, h - 1)
					im.crop(b).save('state/'+str(d)+str(random.random())+'.png')
					return 1000000
				else:
					val += str(d)
	return int(val)

def getState(im):
	col, row = im.size
	pixels = img2gray(im)
	# detectDigit(pixels)
	# im.show()
	# return 
	whitePos = firstWhite(pixels[:, col/2])

	if whitePos >= 85 and whitePos < 90:
		label = 'AllIn'
	elif whitePos >= 103 and whitePos < 110:
		label = 'RangPai'
	elif whitePos:
		img = im.crop((0, whitePos+Geng_height, 79, 308))
		label = getNum(img)
	
	if isinstance(label, int) and label < 0:
		label = 'unknown'
	return label

def main():
	path = "state/all/"
	dirs = os.listdir( path )
	width = 79
	height= 308
	box = (41,1106,41+width,1106+height)
	low = 1

	padding = 0
	width = 19

	for file in dirs:	
		if file[-1] != 'g':
			continue
		print file
		im = Image.open(path+file)
		# im = im.crop(box)
		# print detectDigit(img2gray(im))
		# continue
		try:
			label = getState(im)
			if isinstance(label, int) and label > 100000:
					break
			os.rename(path+file, path+str(label)+"_"+str(random.random())+".png")
		except:
			os.rename(path+file, path+"error_"+str(random.random())+".png")
		# im.save('state/all/'+str(label)+'_'+str(random.random())+'.png')
# 
if __name__ == '__main__':
	main()