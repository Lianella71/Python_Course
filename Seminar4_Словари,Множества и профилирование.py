
# ЗАдача № 1

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# s = "a a a b c a a d c d d"
# print(s.split())
# array = []

# string_ = "a a a b c a a d c d d"
# orig = string_.split()
# newlist = [] 

# count_times = {}

# for symbol in orig:
#     if not symbol in count_times:
#         count_times[symbol] = 1 # Если встретили в первый раз символ, добавляем его в словарь
#         newlist.append(symbol)
#     else:
#         newlist.append(f'{symbol}_{count_times[symbol]}')  # Встретили тот-же символ и присвоили ему значение со счетчика
#         count_times[symbol] += 1

# print(" ".join(newlist))

# ЗАДАЧА № 2

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13
# string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"


# s = set()

# for word in string.split(' '):
#     s.add(word.upper())

# print(len(s))

# ЗАдача № 3

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня 
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# Петя 
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 

# Рабочее решение : 
    
# n = int(input())
# max_number = float("-inf")

# while n != 0:
#     if n == 0:
#         break
#     if max_number < n:
#         max_number = n
#     n = int(input())

# print(max_number)

# Модернизация:
# max_number = float("-inf")

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if max_number < n:
#         max_number = n

# print(max_number)
