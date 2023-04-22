"""Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""


"""def show_menu() -> int:
print("\nВыберите необходимое действие:\n"
"1. Отобразить весь справочник\n"
"2. Найти абонента по фамилии\n"
"3. Найти абонента по номеру телефона\n"
"4. Добавить абонента в справочник\n"
"5. Сохранить справочник в текстовом формате\n"
"6. Закончить работу")
choice = int(input())
return choice"""

import csv

def display_all_records():
    for row in reader:
        print(f'Фамилия: {row[0]}\nимя: {row[1]}\nномер телефона: {row[2]}\nкомментарий: {row[3]}\n')
      
def find_last_name(reader):
    last_name = input('Введите фамилию: ')
    for elem in filter(lambda x: x[0] == last_name, reader):
        print(f'Фамилия: {elem[0]}\nимя: {elem[1]}\nномер телефона: {elem[2]}\nкомментарий: {elem[3]}\n')
    
def find_phone_number(reader):
    phone = input('Введите номер телефона: ')
    return filter(lambda x: x[2] == phone, reader)
def add_abonent():
    with open('phonebook.csv','a',encoding='utf-8',newline=' ') as out_file:
        info = input('Введите данные абонента: ').split()
        csv.writer(out_file).writerow(info)
        
        
for elem in iter(input, '6'):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        
                
        if elem == '1':
            display_all_records()
            
        elif elem == '2':
            print(*find_last_name(reader))
            
        elif elem == '3':
            print(*find_phone_number(reader))  
            
        elif elem == '4':
            add_abonent()
        
def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


"""def read_csv(filename: str) -> list:
data = []
fields = ["Фамилия", "Имя", "Телефон", "Описание"]
with open(filename, 'r', encoding='utf-8') as fin:
for line in fin:
record = dict(zip(fields, line.strip().split(',')))
data.append(record)



return data"""