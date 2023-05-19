# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

def func(list_1, abc):
    res = set()
    for item in list_1:
      count = 0
      for x in item:
        if x in abc:
          count += 1
      res.add(count)
    return res

my_str = input("Введите стих: ")
# my_str = "пара-ра-рам рам-пам-папам па-ра-па-да"

abc = "аеёиоуыэюя"

print("Парам пам-пам" if len(func(my_str.split(), abc)) == 1 else "Пам парам")


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.

def print_operation_table(func, x, y):
   for rows in range(1, x + 1):
    temp_str = ""
    for cols in range(1, y + 1):
      temp_str += f"{func(rows, cols)}  "
    print(temp_str)
      
print_operation_table(lambda x, y: x * y, 6, 6)