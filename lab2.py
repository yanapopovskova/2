"""Нечетные четырехричные числа, не превышающие 409610, у которых третья справа цифра равна 2.
Выводит на экран цифры числа, исключая двойки. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""
import re
numbers = []
answer = []


def w(n):
    numeros = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
               '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
    return numeros.get(n)


with open('test.txt', 'r') as f:
    buff = f.read()
    if not buff:
        print('Файл пуст')
        quit()
    u = re.findall(r'[123]+2[123]{2}', buff)
    for i in u:
        if int(i, 4) < 4096 and int(i) % 2 != 0:
            numbers.append(int(i))
            answer.append(i.replace('2', ''))
    if not numbers:
        print('Нет подходящих цифр')
        quit()
    else:
        print('Цифры чисел без 2:', *answer)
        answer = ''
        for i in str((max(numbers) + min(numbers)) // 2):
            answer += w(i) + ' '
        print('Среднее:', (max(numbers) + min(numbers)) // 2, answer)
