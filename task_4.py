"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no"""

n = int(input("Введите количество долек по длине: "))
m = int(input("Введите количество долек по ширине: "))
k = int(input("Введите количество долек, которые нужно отломить: "))

Flag = 0

if k % m == 0:
    if k / m < n:
        Flag = 1
if Flag == 0:
    if k % n == 0:
        if k / n < m:
            Flag = 1

if Flag == 1:
    print("YES")
else:
    print("NO")