def per_frame_handler(frame_number, output_array, output_count, returned_frame):
	stat = {}

	for output in output_array:
		if output['name'] not in stat:
			stat[output['name']] = {'count' : 0, 'confidence_sum' : 0, 'confidence_avg' : 0}

		stat[output['name']]['count'] += 1
		stat[output['name']]['confidence_sum'] += output['percentage_probability']

	for item in stat:
		if stat[item]['count'] > 0:
			stat[item]['confidence_avg'] = stat[item]['confidence_sum'] / stat[item]['count']

	print(stat)
