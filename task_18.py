"""Задача 18: Требуется найти в массиве A[1..N] самый близкий 
по величине элемент к заданному числу X. Пользователь в первой 
строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка 
содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""
    
import random
import math
X = 25
N = int(input("Введите длину массива > 1: "))
while N < 2:
    print("Введено некорректное значение!")
    N = int(input("Введите длину массива > 1: "))

list_random = [random.randint(1,100) for _ in range(N)]
print(list_random)
dif = abs(X - list_random[0])
i = 0
iMin = 0
while i < len(list_random):
    if dif > abs(X - list_random[i]):
        dif = abs(X - list_random[i])
        iMin = i
    i += 1
print(X)
print(f"-> A[{iMin}]={list_random[iMin]}")