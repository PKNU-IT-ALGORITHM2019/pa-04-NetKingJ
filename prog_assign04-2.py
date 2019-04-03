while True:
  cmd = input("$ ").split()
  if cmd[0] == "exit":
    break
  if cmd[0] == "read":
    f = open(cmd[1], "r")
    lines = f.readlines()
    f.close()
    lines.pop(0) # 첫줄 제거
    list = []
    for line in lines:
      list.append(line.split(','))
    from datetime import datetime
    def str2time(str):
        return datetime.strptime(str[1:], '%d/%b/%Y:%H:%M:%S')
  if cmd[0] == "sort":
    if cmd[1] == "-t":
      cnt = cmd[1]
      list.sort(key=lambda item:str2time(item[1]))
    if cmd[1] == "-ip":
      cnt = cmd[1]
      list.sort(key=lambda item:(item[0], str2time(item[1])))
  if cmd[0] == "print":
    if cnt == "-t":
      for i in list:
          print(i[1][1:]) # 앞의 [ 제거
          print('\tIP:', i[0])
          print('\tURL:', i[2])
          print('\tStatus:', i[3])
    if cnt == "-ip":
      for i in list:
          print(i[0])
          print('\tTime:', i[1][1:]) # 앞의 [ 제거
          print('\tURL:', i[2])
          print('\tStatus:', i[3])
