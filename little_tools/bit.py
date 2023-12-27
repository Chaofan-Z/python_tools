from cProfile import label

"""
增加内外流流量判断
"""
def analysis_sctr_label(label_value):
  result = ""
  # print(label_value)
  label_value = bin(label_value)[2:][::-1]
  # print(label_value)

  if label_value[0] == '0':
    result += "外流_"
  else :
    result += "内流_"

  if label_value[1] == '0':
    result += "内流负样本_"
  else :
    result += "内流正样本_"

  if label_value[2] == '0':
    result += "外流负样本_"
  else :
    result += "外流正样本_"

  if label_value[3] == '0':
    result += "首页_"
  else :
    result += "非首页_"

  pos = int(label_value[4:][::-1], 2)
  result += "位置{}".format(pos - 1)
  return result


"""
原来逻辑
"""
def analysis_sctr_label2(label_value):
  result = ""
  # print(label_value)
  label_value = bin(label_value)[2:][::-1]
  # print(label_value)

  if label_value[0] == '0':
    result += "内流负样本_"
  else :
    result += "内流正样本_"

  if label_value[1] == '0':
    result += "外流负样本_"
  else :
    result += "外流正样本_"

  if label_value[2] == '0':
    result += "首页_"
  else :
    result += "非首页_"

  pos = int(label_value[3:][::-1], 2)
  result += "位置{}".format(pos - 1)
  return result


data_result = {}
data_result2 = {}

# analysis_sctr_label(10)
with open("./label_extractor") as file:
  for line in file:
    data_result[analysis_sctr_label(int(line.strip().split(']')[-1].split(':')[0].strip()))] \
        = int(line.strip().split(']')[-1].split(':')[1].strip())
for key in data_result:
  print(key, data_result[key])

print("=" * 50)

with open("./label_extractor2") as file:
  for line in file:
    data_result2[analysis_sctr_label2(int(line.strip().split(']')[-1].split(':')[0].strip()))] \
        = int(line.strip().split(']')[-1].split(':')[1].strip())
for key in data_result2:
  print(key, data_result2[key])