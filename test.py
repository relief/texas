import Image
import cv2
import numpy

# read raw_data to im
mode = 'RGBA'
size = (1080, 1920)
f = open('data/screenshot.raw', 'rb')
f.read(12)

nparr = numpy.fromstring(f.read(), numpy.uint8)
print nparr
img_np = cv2.imdecode(nparr, 1)

# CV
img_ipl = cv2.cv.CreateImageHeader((1080, 1920), cv2.cv.IPL_DEPTH_8U, 3)
cv2.cv.SetData(img_ipl, img_np)


#im.show()
# cimg = cv2.cv.CreateImageHeader(im.size,cv2.IPL_DEPTH_8U,3)    #CV Image
# open_cv_image = numpy.array(im) 
# open_cv_image = cv2.cvtColor(open_cv_image, cv2.cv.CV_RGBA2BGR)

# cv2.cv.SetData(cimg,open_cv_image)

cv2.cv.NamedWindow('cimg')
cv2.cv.ShowImage('cimg',img_ipl)
cv2.cv.WaitKey()

# im.save('123.png')
# contrast = cv2.imread('123.png')