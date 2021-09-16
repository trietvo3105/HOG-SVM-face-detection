import numpy as np

def nms_slow(boxes,overlapthresh):
	if len(boxes) == 0:
		return []

	pick = []

	x1 = boxes[:,0]
	y1 = boxes[:,1]
	x2 = boxes[:,2]
	y2 = boxes[:,3]

	area = (x2-x1+1)*(y2-y1+1)
	idxs = np.argsort(y2)

	while len(idxs) > 0:
		last = len(idxs) - 1
		i = idxs[last]
		pick.append(i)
		suppress = [last]

		for pos in range(0, last):
			
			j = idxs[pos]
 	
			xx1 = max(x1[i], x1[j])
			yy1 = max(y1[i], y1[j])
			xx2 = min(x2[i], x2[j])
			yy2 = min(y2[i], y2[j])
 	
			w = max(0, xx2 - xx1 + 1)
			h = max(0, yy2 - yy1 + 1)
 
			overlap = float(w * h) / area[j]

			if overlap > overlapthresh:
				suppress.append(pos)
 
		idxs = np.delete(idxs, suppress)

	return boxes[pick]
		


'''
x = [3,1,5,0,1.2,10,12,11]
y = np.argsort(x)
last = len(y)-1
print(y)
print(len(y))
print(last)
print(y[last])
last -= 1
print(last)
print(y[last])'''