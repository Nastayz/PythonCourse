""""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

while S < 2 or S >= 2000 or P <= 0 or P >=1000000:
    print("Введены некорректные значения!")
    S = int(input("Введите сумму чисел: "))
    P = int(input("Введите произведение чисел: "))

n = 1   # число 1
m = 1   # число 2
f = 0   # флаг, означающий, что числа попадают под оба условия (сумма и произведение)
for i in range(1,S-1):
    n = i
    m = S - n
    if P == n * m:
        f = 1
        break
    
    i += 1
    
if f == 1:
    print(f"n = {n}, m = {m}")
else:
    print(f"Нет таких натуральных чисел")