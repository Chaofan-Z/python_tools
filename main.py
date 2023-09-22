from data_tools.data_utils import *

# draw_histogram("./data_files/lps_cvr_by_exp.csv", 
#   key_column="expname", key_value=['base1', 'exp6'], data_column='cvr'
#   ,bins_number=100, is_log=True)

# draw_histogram("./data_files/lps_cvr_by_pos.csv", sep=',',
#   key_column="pos", key_value=[0], data_column='cvr'
#   ,bins_number=100, is_log=True)

key_column="pos"
key_value=[1]
data_column='cvr'

draw_histogram("./data_files/lps_cvr_by_pos_exp6.csv", sep='\t',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="exp", is_log=True)

draw_histogram("./data_files/lps_cvr_by_pos_base1.csv", sep='\t',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="exp", is_log=True)

import matplotlib.pyplot as plt
plt.show()
