# n = 700
# m = 701
# # output = m//n + int (m/m%n)
# output = (m - 1) // n + 1
# print(output)

# a = 20
# b = 21
# c = 23
# d = 2

# output = (a+1)//d + (b+1)//d + (c+1)//d
# print(output)

# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input('Сколько вагонов прошел Витя: '))
# j = int(input('В каком вагоне оказался: '))

# output = j + i - 1
# #output2 = j   
# if i == j :
#     print('Недостаточно информации')
# else :
#     print(f'{output} C хвоста')

# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES
# i = int(input('Введите год '))
# if i%4 == 0 and i%100 != 0 or i%400 == 0:
#     print('Год високосный')
# else:
#     print('Год не високосный')