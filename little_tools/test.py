with open("./test") as file:
  a = 0
  b = 0
  for line in file:
    b += int(line.strip().split(" ")[1])
    if "外流_内流正样本" in line:
      a += int(line.strip().split(" ")[1])
  print(a / b)
