import os
from imageai.Detection import VideoObjectDetection
import analysis_perframe as pfh

def test_default(path_in, path_out, path_model = os.path.join(os.getcwd() , 'models\\yolo.h5'), speed = 'fast'):
	detector = VideoObjectDetection()
	detector.setModelTypeAsYOLOv3()
	detector.setModelPath(path_model)

	detector.loadModel(detection_speed = speed) #fast, faster, fastest, flash

	detector.detectObjectsFromVideo(
		input_file_path = path_in,
		output_file_path = path_out + '_default',
		frames_per_second = 20,
		per_frame_function = pfh.per_frame_handler,
		minimum_percentage_probability = 30,
		return_detected_frame = True
	)
