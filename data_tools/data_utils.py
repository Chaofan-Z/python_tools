import enum
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



"""
-- DATA FORMAT --
expname	cvr
base1	0.001897536
exp6	9.15009E-06
exp6	4.39412E-05
base1	9.08746E-05
exp6	0.000883182
"""
def read_csv1(filename, key_column, key_value):
  file_data = pd.read_csv(filename, sep=",").dropna()
  process_data = []
  for key in key_value:
    process_data.append(file_data[file_data[key_column] == key].dropna())
  # base1_data = file_data[file_data['expname'] == 'base1']
  # exp6_data = file_data[file_data['expname'] == 'exp6']
  return process_data

"""
data : 单列data_frame
bins_number : 分桶数量
"""
def get_data_bins(data, bins_number):
  bins = np.histogram_bin_edges(data, bins=bins_number)
  return bins

def draw_histogram(filename, key_column = 'expname', key_value = ['base1', 'exp6'], data_column = 'cvr', bins_number = 100, is_log=False):
  process_data = read_csv1(filename, key_column, key_value)
  if is_log:
    for i in range(len(process_data)):
      process_data[i][data_column] = np.log(process_data[i][data_column])

  # 得到两组数据的分桶
  # base_bins = get_data_bins(base_data[data_column], bins_number)
  # exp_bins = get_data_bins(exp_data[data_column], bins_number)

  for i, data in enumerate(process_data):
    plt.hist(data[data_column], bins=bins_number, alpha=0.5, label='{0}_{1}_hist'.format(key_column, key_value[i]))

  plt.xlabel(data_column)
  plt.ylabel('Frequency')
  plt.legend(loc='upper right')
  plt.title('Frequency Distribution of Lps cvr')
  plt.show()
