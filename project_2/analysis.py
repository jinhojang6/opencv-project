import os
import matplotlib.pyplot as plt
%matplotlib inline

from test_default import test_default
from test_improved import test_improved
import analysis_stastics

execution_path = os.getcwd()
filename = 'PopeVisitToKorea.mp4'

words = filename.split('.')
filename_short = '.'.join(words[:len(words) - 1])

path_in = os.path.join(execution_path, 'videos\\', filename)
path_out = os.path.join(execution_path, 'results\\', filename_short)

analysis_stastics.stats = analysis_stastics.stastics()
test_default(path_in, path_out)
test_improved(path_in, path_out)

print(analysis_stastics.stats.get_avg())
