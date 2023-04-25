def read_int(arg = "число"):
    return int(input(f"Введите {arg}: "))

def read_list(arg = "список"):
   string = input(f"Введите {arg}: ")
   list_1 = "".join("".join(string.split("[")).split("]")).split(",")
   return list_1

def fill_list(list_1: list = [1], d = 1, c = 1):
    for i in range(c - 1):
      list_1.append(list_1[i] + d)
    return list_1

def check_lists(list_1: list, range_1:list):
  temp_list = list()
  for i in range(len(list_1)):
    if (int(range_1[0]) <= int(list_1[i]) <= int(range_1[1])):
      temp_list.append(i)
  return temp_list