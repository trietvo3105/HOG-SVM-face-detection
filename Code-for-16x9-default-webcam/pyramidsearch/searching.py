# import the necessary packages
import imutils

def pyramid_scale(image, scale, minSize=(64,128)):
	# yield the original image
	yield image

	# keep looping over the pyramid
	while True:
		# compute the new dimensions of the image and resize it
		weight = int(image.shape[1] / scale)
		image = imutils.resize(image, width=weight)

		# if the resized image does not meet the supplied minimum
		# size, then stop constructing the pyramid
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break

		# yield the next image in the pyramid
		yield image

def windows_slide(image, steps, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], steps):
		for x in range(0, image.shape[1], steps):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])