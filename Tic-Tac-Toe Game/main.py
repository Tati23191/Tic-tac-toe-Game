field = [['-']*3 for _ in range(3)]

def func_field(f):
  print(' 0 1 2')
  for i in range(len(field)):
    print(str(i), *field[i])

#опрос
def move(f):
  while True:
    place = input(f'Ходит {user} .Введите координаты: ').split()
    if len(place) !=2:
      print('Введите две координаты через пробел')
      continue
    if not(place[0].isdigit() and place[1].isdigit()):
      print('Введите числа')
      continue
    a,b = map(int, place)
    if not(a >= 0 and b >= 0 and b < 3):
      print('Введите числа от 0 до 2')
      continue
    if f[a][b] != '-':
      print('Клетка занята')
      continue 
    break
  return a,b
  
#результаты
def win_position(f, user):
  f_list = []
  for l in f:
    f_list += l
  positions = [[0, 1, 2],[3, 4, 5], [6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
  index_u = set([i for i, x in enumerate(f_list) if x == user])
  for p in positions:
    if len(index_u.intersection(set(p)))==3:
      return True
  return False

#вывод поля
count = 0
while True:  
  func_field(field)  
  if count%2==0:
    user = 'х'
  else:
    user = 'o'
  a,b = move(field)
  field[a][b] = user
  if count == 9:
    print('Ничья')
  if win_position(field, user):
    print(f"Выйграл {user}")
    func_field(field)
    break    
  count+=1
      





