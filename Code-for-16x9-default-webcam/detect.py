import cv2
from imutils import paths
from sklearn.externals import joblib
import imutils
import numpy as np
from pyramidsearch.searching import pyramid_scale
from pyramidsearch.searching import windows_slide
from train import get_hog
from nms import nms_slow

def detect(img):
	filename = 'svm_model_4.model' 
	img = imutils.resize(img, width = min(800, img.shape[1]))
	image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	(winW, winH) = (64,128)
	clf = joblib.load(filename)
	boxes = []
	scale = 1.5
	const = 0
	count = 0
	gethog = get_hog()

	for resized in pyramid_scale(image, scale=scale):
		# loop over the sliding window for each layer of the pyramid
		for (x, y, win) in windows_slide(resized, steps=8, windowSize=(winW, winH)):
			# if the window does not meet our desired window size, ignore it
			if win.shape[0] != winH or win.shape[1] != winW:
				continue
			fd = gethog.compute(win)
			fd = fd.reshape(1, -1)
			pred = clf.predict(fd)
			
			if pred == 1:
				boxes.append((int(x * (scale**const)),int(y * (scale**const)),int((x+winW) * (scale**const)),int((y+winH) * (scale**const))))
		const += 1
	boxes = np.squeeze(boxes)
	orig = img.copy()

	for (startX,startY,endX,endY) in boxes:
		cv2.rectangle(orig, (startX,startY), (endX,endY), (0,0,255), 2)

	pick = nms_slow(boxes,0.3)
	for (startX,startY,endX,endY) in pick:
		cv2.rectangle(img, (startX,startY), (endX,endY), (0,255,0), 2)
		count = count + 1
	return count,img

