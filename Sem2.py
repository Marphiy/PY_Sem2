import random
from random import randint

def Zadacha11():  # 11. Напишите программу, которая принимает на вход число N и выдаёт
    # последовательность из N членов.
    n = int(input('N = '))
    # num1 = 1
    # for i in range(n):
    #     print(num1, end = ' ')
    #     num1 *= -3
    # print()
    a = [(-3) ** i for i in range(n)]
    print(a)


def Zadacha12():  # 12. Для натурального n создать список, состоящий из элементов
    # последовательности 3n + 1.
    n = int(input('N = '))
    list = []
    for i in range(1, n+1):
        num1 = 3 * i + 1
        list.append(num1)
    print(list)
    # a = [3 * i + 1 for i in range(1, n + 1)]
    # print(a)


def Zadacha13():  # Напишите программу, в которой пользователь будет задавать две
    # строки, а программа - определять количество вхождений одной строки в другой.
    str1 = input('Введите строку 1: ')
    str2 = input('Введите строку 2: ')
    # for i in range(len(str1)):
    #     count1 = 0
    #     for j in range(len(str2)):
    #         if str2[j] == str1[i]:
    #             count1 += 1
    #     print(f'"{str1[i]}" встречается во второй строке {count1} раз')
    # print()
    # for i in range(len(str2)):
    #     count2 = 0
    #     for j in range(len(str1)):
    #         if str1[j] == str2[i]:
    #             count2 += 1
    #     print(f'"{str2[i]}" встречается в первой строке {count2} раз')

    # print(f'Строка 2 встречается в 1й строке {str1.count(str2)} раз/а')

    count = 0
    k = 1
    # for i in range(0, len(str1) - len(str2) + 1, k):
    #     if str2 in str1[i: i + len(str2)]:
    #         count += 1
    #         i += len(str2)
    # else:
    #     k = 1
    i = 0
    while i < len(str1) - len(str2) + 1:
        if str2 in str1[i: i + len(str2)]:
            count += 1
            i += len(str2)
        else:
            i += 1
    print(count)


def Zadacha14():  # 14. Напишите программу, которая принимает на вход
    # вещественное число и показывает сумму его цифр.
    num = input('Введите вещественное число: ')
    sum = 0
    for i in range(len(num)):
        if num[i] != '.' and num[i] != ',':
            sum += int(num[i])
    print(sum)


def PowFrom1toN(n):
    newPow = 1
    for i in range(1, n + 1):
        newPow *= i
    return newPow 

        
def Zadacha15():  # 15. Напишите программу, которая принимает на вход
    # число N и выдает набор произведений чисел от 1 до N.
    num = int(input('Введите число от 1 до 10: '))
    list = []
    for j in range(1, num + 1):
        list.append(PowFrom1toN(j))
    print(list)

def Random_fill_list(size, limfrom, limto):
    list = []
    for i in range(size):
        list.append(randint(limfrom, limto))
    return list    
    
    
    
def Zadacha16(): # 16. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите 
    # на экран их сумму.
    n = int(input('Введите число n: '))
    list = [(1 + 1/i) ** i for i in range(1, n + 1)]
    print(list)
    sum = 0
    for i in list:
        sum += i
    print(f'Сумма элементов списка = {sum}')
    
def Zadacha17(): # 17. Задайте число N, создайте список, заполненный из промежутка: [-N, N]. 
    # Найдите произведение элементов на указанных позициях. Позиции (случайные)  хранятся в 
    # файле file.txt (создаётся во время выполнения кода и зависит от количества элементов 
    # в списке) в одной строке одно число.
    n = int(input('Введите число n: '))
    list = [i for i in range(-n, n+1)]
    print(f'Список чисел от -n до n: {list}')
    print('Формируем список, состоящий из 3х элементов, определяющих индексы\nэлементов исходного списка (-n : n) в случайном порядке:')
    FILETXT_SIZE = 3
    filetxt = Random_fill_list(FILETXT_SIZE, 0, 9)
    print(filetxt)
    print('cоздаем file1.txt...')
    f1 = open('text1.txt', 'w')
    print('копируем индексы в file1.txt....')
    f1.writelines("%s\n" % i for i in filetxt)
    f1.close()
    print('Построчно копируем данные из text1.txt в список индексов.....')
    f = open('text1.txt')
    index_list = f.readlines()
    for i in range(len(index_list)):
        index_list[i] = int(index_list[i][-2])
    print(index_list)
    print(f'Произведение элементов исходного списка с индексами ', end = '')
    new_pow = 1
    for i in index_list:
        new_pow *= list[i]
        print(i, end = ' ')
    print(f'= {new_pow}')
        
def Zadacha18(): # Реализуйте алгоритм перемешивания списка.
    list = Random_fill_list(10, 0, 100)
    print(f'Формируем список случайных чисел из 10 элементов:\n{list}')
    random.shuffle(list)
    print(f'Перемешиваем список:\n{list}')
    


# Zadacha11()
# Zadacha12()
# Zadacha13()
# Zadacha14()
# Zadacha15()
# Zadacha16()
# Zadacha17()
# Zadacha18()
