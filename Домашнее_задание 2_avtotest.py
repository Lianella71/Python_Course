# Задача № 1
# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
# чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, 
# и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
# -------------------------------------------------------------------------------------------------------------------

# coins = [0, 0, 1, 0, 1, 0, 0]
# count = 0
# n = len(coins)
# for i in range(n):
#     if coins[i] == 1:
#         count +=1
#     i+=1    
# if count >= n-count:
#     print(n-count)
# else:
#     print(count)

# ----------------------------------------------------------------------------------------------------------------

# Задача № 2
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
# ------------------------------------------------------------------------------------------------------------

# S = 12
# P = 27
# x = 1   
# y = 1   
# f = 0   
# for i in range(1,S-1):
#     x = i
#     y = S - x
#     if P == x * y:
#         f = 1
#         break    
#     i += 1    
# if f == 1:
#     print(x, y)
# else:
#     print(f"Нет таких натуральных чисел")

# -----------------------------------------------------------------------------------------------------------

# Задача № 3
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# --------------------------------------------------------------------------------------------------------
# N = 16
# k = 0
# while 2**k <= N:
#   print(2**k)
#   k += 1
# print()