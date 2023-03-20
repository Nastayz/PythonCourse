"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""

import random

n = int(input("Введите количество монет: "))
A = []
count = 0
for i in range(n):
    A.append(random.randint(0,1))
    # print(A)
    if A[i] == 1:
        count +=1
    i+=1
    
print(A)

if count >= n-count:
    print(f"Нужно перевернуть {n-count} монет")
else:
    print(f"Нужно перевернуть {count} монет")



