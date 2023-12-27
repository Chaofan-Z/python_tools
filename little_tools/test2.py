with open("./test2") as file:
  a = 0
  b = 0
  for line in file:
    # b += int(line.strip().split(" ")[1])
    a, b = line.strip().split(" ")
    a = a.split("_")
    a = a + [b]
    print('\t'.join(a))
