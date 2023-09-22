from data_tools.data_utils import *

# draw_histogram("./data_files/lps_cvr_by_exp.csv", 
#   key_column="expname", key_value=['base1', 'exp6'], data_column='cvr'
#   ,bins_number=100, is_log=True)

draw_histogram("./data_files/lps_cvr_by_pos.csv", 
  key_column="pos", key_value=[0,1,2,5,6,7,8], data_column='cvr'
  ,bins_number=100, is_log=True)