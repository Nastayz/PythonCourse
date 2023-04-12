"""Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам 

Вывод: Парам пам-пам"""


poem = "пара-ра-рам рам-пам-папам па-ра-па-дам"
poem = list(poem.split())
print(poem)
vowelLetters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

syllables = []
for word in poem:
    cntSyl = len(list(filter(lambda i: i in vowelLetters, word)))
    syllables.append(cntSyl)
    
cntSyl = 0
for i in range(len(syllables)):
    if syllables[i] == syllables[0]:
        cntSyl += 1
        
if len(syllables) == cntSyl:
    print('Парам пам-пам')
else:
    print('Пам парам')