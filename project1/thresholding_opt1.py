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
			ret, thresh_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
			M1 = np.sum(thresh_image) / 255
			M0 = np.size(thresh_image) - M1
			diff_sum += abs(M0 - M1)
			ret, img = cap.read()

	print(f'thresh {threshold}: {diff_sum}, eslapsed time: {time.time() - timeP}s')
	return diff_sum

def evaluate_section(path, value_list, init = 0, end = 255, div = 4):
	div = min(div, end - init)
	thresh_list = [0] * (div + 1)
	eval_list = [0] * (div + 1)
	for index in range(div + 1):
		threshold = init + ((end - init) * index // div)
		thresh_list[index] = threshold
		if value_list[threshold] < 0:
			value_list[threshold] = evaluate_threshold(path, threshold)
		eval_list[index] = value_list[threshold]

	for index in range(div + 1):
		if index == div:
			index_min = index
			break
		if eval_list[index + 1] > eval_list[index]:
			index_min = index
			break

	if div == (end - init):
		return thresh_list[index_min], eval_list[index_min]
	else:
		return evaluate_section(path, value_list, thresh_list[max(0, index_min - 1)], thresh_list[min(div, index_min + 1)])

video_file = "./data/butterflies.mp4"
cap = cv2.VideoCapture(video_file)

print(f'frame size: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} by {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
print(f'frame count: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}')
print(f'pixel count: {cap.get(cv2.CAP_PROP_FRAME_WIDTH) * cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * cap.get(cv2.CAP_PROP_FRAME_COUNT) / 1000000}M')

timeI = time.time()
thresh_opt = 0
diff_opt = -1

value_list = [-1] * 256
thresh_opt, diff_opt = evaluate_section(video_file, value_list)

print(f'total eslapsed time: {time.time() - timeI}s')
print(f'optimal threshold: {thresh_opt} at diff_sum {diff_opt}')
