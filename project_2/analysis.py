import os
import matplotlib.pyplot as plt
import analysis_perframe as pfh

import yolo_utils

from imageai.Detection import VideoObjectDetection
import imageai
%matplotlib inline

execution_path = os.getcwd()
filepath = 'drone_01.mp4'

words = filepath.split('.')
filename = '.'.join(words[:len(words) - 1])

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , 'models\\yolo.h5'))

detector.loadModel(detection_speed = 'fast') #fast, faster, fastest, flash

detector.detectObjectsFromVideo(
	input_file_path = os.path.join(execution_path, 'videos\\', filepath),
	output_file_path = os.path.join(execution_path, 'results\\', filename),
	frames_per_second = 20,
	per_frame_function = pfh.per_frame_handler,
	minimum_percentage_probability = 30,
	return_detected_frame = True
)

try:
	vid = cv.VideoCapture(FLAGS.video_path)
	height, width = None, None
	writer = None
except:
	raise 'Video cannot be loaded!\n\
					   Please check the path provided!'

finally:
	while True:
		grabbed, frame = vid.read()

		# Checking if the complete video is read
		if not grabbed:
			break

		if width is None or height is None:
			height, width = frame.shape[:2]

		frame, _, _, _, _ = infer_image(net, layer_names, height, width, frame, colors, labels, FLAGS)

		if writer is None:
			# Initialize the video writer
			fourcc = cv.VideoWriter_fourcc(*"MJPG")
			writer = cv.VideoWriter(FLAGS.video_output_path, fourcc, 30,
							(frame.shape[1], frame.shape[0]), True)


		writer.write(frame)

	print ("[INFO] Cleaning up...")
	writer.release()
	vid.release()
