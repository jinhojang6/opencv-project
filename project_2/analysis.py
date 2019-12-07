import os
import matplotlib.pyplot as plt
%matplotlib inline

from test_default import test_default
from test_improved import test_improved

execution_path = os.getcwd()
filepath = 'drone_01.mp4'

words = filepath.split('.')
filename = '.'.join(words[:len(words) - 1])

path_in = os.path.join(execution_path, 'videos\\', filepath)
path_out = os.path.join(execution_path, 'results\\', filename)

test_default(path_in, path_out)
test_improved(path_in, path_out)
