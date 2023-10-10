from data_tools.data_utils import *
import matplotlib.pyplot as plt

# draw_histogram("./data_files/lps_cvr_by_exp.csv", 
#   key_column="expname", key_value=['base1', 'exp6'], data_column='cvr'
#   ,bins_number=100, is_log=True)

# draw_histogram("./data_files/lps_cvr_by_pos.csv", sep=',',
#   key_column="pos", key_value=[0], data_column='cvr'
#   ,bins_number=100, is_log=True)

"""
key_column="pos"
key_value=[6,7,8]
data_column='cvr'

# LPS 分exp，观察各个位置的预估值分布变化
draw_histogram("./data_files/lps_cvr_concat_by_pos_exp6.csv", sep=',',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="exp", is_log=True)

draw_histogram("./data_files/lps_cvr_concat_by_pos_base1.csv", sep=',',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="base", is_log=True)

plt.show()

"""
# key_column="expname"
# key_value=['base1','exp3','exp4']
# data_column='cvr'

key_column="pos"
key_value=[1,2,5]
data_column='cvr'

draw_histogram("./data_files/conv_cvr_by_pos_base1.csv", sep=',',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="base1", is_log=True)

draw_histogram("./data_files/conv_cvr_by_pos_exp3.csv", sep=',',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="exp3", is_log=True)

draw_histogram("./data_files/conv_cvr_by_pos_exp4.csv", sep=',',
  key_column=key_column, key_value=key_value, data_column=data_column,
  bins_number=100, draw_flag="exp4", is_log=True)

plt.show()


"""
line_visibility = {line1: True, line2: True}

# 创建一个交互式的图例
leg = ax.legend(loc='upper left')

# 定义一个函数，用于切换曲线的可见状态
def on_legend_click(event):
    line = event.artist
    if line in line_visibility:
        line_visibility[line] = not line_visibility[line]
        line.set_visible(line_visibility[line])
        plt.draw()

# 将交互式图例的点击事件绑定到切换函数上
leg.set_picker(5)  # 设置点击图例的触发距离
fig.canvas.mpl_connect('pick_event', on_legend_click)

plt.show()
"""