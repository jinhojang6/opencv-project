import sys
import time
import numpy as np
import cv2
print(sys.executable)
print(sys.version)
print(cv2.__version__)

video_file = "./data/butterflies.mp4"
cap = cv2.VideoCapture(video_file)

print(f'frame size: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} by {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
print(f'frame count: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}')
print(f'pixel count: {cap.get(cv2.CAP_PROP_FRAME_WIDTH) * cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * cap.get(cv2.CAP_PROP_FRAME_COUNT) / 1000000}M')

timeI = time.time()
timeP = time.time()
thresh_current = 0
thresh_opt = 0
diff_opt = -1

for thresh_current in range(0, 256):
	cap = cv2.VideoCapture(video_file)
	diff_sum = 0
	if cap.isOpened():
		ret, img = cap.read()
		while ret:
			gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			ret, thresh_image = cv2.threshold(
				gray_image, thresh_current, 255, cv2.THRESH_BINARY)
			M1 = np.sum(thresh_image) / 255
			M0 = np.size(thresh_image) - M1
			diff_sum += abs(M0 - M1)
			ret, img = cap.read()

	print(
		f'thresh {thresh_current}: {diff_sum}, eslapsed time: {time.time() - timeP}s')
	timeP = time.time()
	if (diff_opt < 0) or (diff_opt > diff_sum):
		thresh_opt = thresh_current
		diff_opt = diff_sum
		print('new optimal')

print(f'total eslapsed time: {time.time() - timeI}s')
print(f'optimal threshold: {thresh_opt} at diff_sum {diff_opt}')
