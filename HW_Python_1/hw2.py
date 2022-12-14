# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# print('Введите число:')
# number=int(input())
# number1=str(number)
# count=len(number1)
# print(count)
# remain=0
# result=0

# for item in count:
#     remain = number - number % 10
#     result = result + (number - remain)
#     number = number / 10
#     item =+1
# print(result)

# n=input('введите число')
# sum = 0
# for i in n:
#     if i != '.':
#         sum += int(i)

# print(sum)


# произведения цифр числа N

n=int(input('введите число'))
result = 1
for i in range(1, n + 1):
    result = result * i
    print(result)