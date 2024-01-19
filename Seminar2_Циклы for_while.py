# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120



# Числа Фибоначчи
# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2)

# A = int(input('Ввведите число А: '))
# number = 3
# f1 = 1
# f2 = 1
# while f2 < A:
#     f1, f2 = f2, f1+f2
#     number += 1
# if f2 == A:
#     print(number)
# else:
#     print(-1)

    
# n = int(input("ВВедите число: "))
# num1 = 0
# num2 = 1
# count = 2
# array = [num1, num2]

# while count <= n:
#     next_num = num1 + num2
#     num1 = num2
#     num2 = next_num
#     array.append(next_num)

#     count += 1


# print(array)

# if n in array:
#     text = "Input num {0} is {1} belong Fibonacci".format(n, array.index(n))
#     print(text)
# else:
#     text = "Input num {0} is {1} dont belong Fibonacci".format(n, -1)
#     print(text)
# --------------------------------------------------------------------------------------------

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# import random
# day = int(input("Введите количество дней => "))
# hi_temp = 0
# num = 1
# while day >= num:
#     temp_in = random.randint(-50, 50)
#     print(f"температура день {num} => {temp_in}")
#     if temp_in > 0 and hi_temp < temp_in:
#         hi_temp = num
#     num += 1
# print(f"Самая высокая температура => день {hi_temp}")

# import random
# put = int(input('Введите количество дней: '))
# count = 0
# temp = 0
# while put != 0:
#     temp = random.randint(-50, 50)
#     print(temp)
#     if 0 < temp:
#         count = count + 1
#     put = put - 1
# print("Количество теплых дней: ")
# print(count) 
#-----------------------------------------------------------------------------------  

# Задача про арбузы

# import random # Импортировать в начале

# n = int(input('введите число N: '))
# min_ = float('inf')
# max_ = float('-inf')

# for i in range(1, n + 1):
#     mass = random.randint(1,51)
    
#     print(f"Арбуз номер {i} имеет массу {mass}")
#     if mass > max_:
#         max_ = mass
#     if mass < min_:
#         min_ = mass
        
# print (f"max= {max_}, min = {min_}")
