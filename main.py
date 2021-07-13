"""
This script should be run to produce the DSML and RESL measures for all subdirectories in data_path.
For elaborated documentation - see: https://github.com/AmirIvry-aka-AI/DSML-and-RESL-measures/tree/main
Copyright (c) 2021 Amir Ivry
"""
from utils import parse_files_from_path, read_wav_files, save_and_plot
from evaluation_metrics import calc_resl_dsml
import os
import warnings
warnings.filterwarnings('ignore')


data_path = 'Demo'
patterns = ('near_end_speech', 'res_input', 'res_prediction')

log_file = open(os.path.join(data_path, 'evaluation_metrics.txt'), 'w')
paths_list = parse_files_from_path(data_path, patterns=patterns)
for path_list in paths_list:
    wav_raw_data, fs = read_wav_files(path_list, patterns=patterns, plot=True)
    resl, dsml = calc_resl_dsml(wav_raw_data, fs, compensate=True)
    log_file = save_and_plot(resl, dsml, path_list, log_file)
log_file.close()
