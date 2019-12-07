class frame_stat:
	def __init__(self):
		self.output_list = []
		self.output_stat = {}

	def add_output(self, output_array):
		self.output_list += output_array

	def get_stat(self):
		stat = {}

		for output in self.output_list:
			if output['name'] not in stat:
				stat[output['name']] = {'count' : 0, 'confidence_sum' : 0, 'confidence_avg' : 0}

			stat[output['name']]['count'] += 1
			stat[output['name']]['confidence_sum'] += output['percentage_probability']

		for item in stat:
			if stat[item]['count'] > 0:
				stat[item]['confidence_avg'] = stat[item]['confidence_sum'] / stat[item]['count']

		return stat
