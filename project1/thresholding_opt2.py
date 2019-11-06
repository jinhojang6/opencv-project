import sys
import time
import numpy as np
import cv2
print(sys.executable)
print(sys.version)
print(cv2.__version__)

def evaluate_threshold(path, threshold):
	cap = cv2.VideoCapture(video_file)
	timeP = time.time()
	diff_sum = 0
	if cap.isOpened():
		ret, img = cap.read()
		while ret:
			gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			ret, thresh_image = cv2.threshold(
				gray_image, threshold, 255, cv2.THRESH_BINARY)
			M1 = np.sum(thresh_image) / 255
			M0 = np.size(thresh_image) - M1
			diff_sum += abs(M0 - M1)
			ret, img = cap.read()

	print(f'thresh {threshold}: {diff_sum}, eslapsed time: {time.time() - timeP}s')
	return diff_sum


def evaluate_section(path):
	start = 0
	end = 255

	while start < end:
		threshold = (start + end) // 2
		current = evaluate_threshold(path, threshold)
		before = current -  evaluate_threshold(path, threshold - 1)
		after = evaluate_threshold(path, threshold + 1) -  current

		if before * after > 0 and before > 0 and after > 0:
			end = threshold

		elif before * after > 0 and before < 0 and after < 0:
			start = threshold + 1

		else:
			return threshold, current

	return -1

video_file = "./data/butterflies.mp4"
cap = cv2.VideoCapture(video_file)

timeI = time.time()
thresh_opt, diff_opt = evaluate_section(video_file)

print(f'total eslapsed time: {time.time() - timeI}s')
print(f'optimal threshold: {thresh_opt} at diff_sum {diff_opt}')
