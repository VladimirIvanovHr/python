# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n=input('введите число')
# sum = 0
# for i in n:
#     if i != '.':
#         sum += int(i)

# print(sum)


# произведения цифр числа N

# n=int(input('введите число'))
# result = 1
# for i in range(1, n + 1):
#     result = result * i
#     print(result)

#Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n=int(input('введите число'))
# # sum = 0
# for i in range (1, n + 1): 
#     sum = sum + (1+1/i)**i
#     print(sum)

# Реализуйте алгоритм перемешивания списка.

import random
list_one = [1, 2, 3, 4, 5]
random.shuffle(list_one)
print(list_one)
