# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('Эта программа принимает на вход число N и ')
n = int(input('Пожалуйста введите число N - '))

lst = {a: round((1+1/a)**a ,3) for a in range(1, n+1)}
print(lst)