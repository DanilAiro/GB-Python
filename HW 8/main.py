# w - перезапись
# r - чтение
# a - дозапись
# r+ - чтение + запись
# b - байт

import funcs

is_active = True

while is_active:
  print("[1] Показать список")
  print("[2] Добавить запись")
  print("[3] Редактировать запись")
  print("[4] Удалить запись")
  print("[5] Поиск")
  print("[6] Выход")
  print()
  res = int(input("Введите номер задачи: "))

  if res == 1:
    funcs.show_contacts()
  elif res == 2:
    funcs.add_contact()
  elif res == 3:
    funcs.edit_contact()
  elif res == 4:
    funcs.delete_contact()
  elif res == 5:
    funcs.search()
  elif res == 6:
    is_active = False
  else:
    print("Ошибка")