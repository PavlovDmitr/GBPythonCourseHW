# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


print('Введите число - день недели или ctrl-c для выхода))')
while True:
    if input() in ['6' , '7']: print('да') 
    else: print('нет')