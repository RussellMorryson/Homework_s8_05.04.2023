"""Задача №49. 
Создать телефонный справочник с возможностью импорта и 
экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, 
которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для 
поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. 
Ваша программа не должна быть линейной """

"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных."""

import re

def Show_data():
  with open('data.txt', 'r', encoding='utf-8') as file:
    book = file.read()
  return book

def Add_line_in_data():
  with open('data.txt', 'a', encoding='utf-8') as file:
    first_name = (input('Введите имя: \n>>> '))
    second_name = (input('Введите фамилию: \n>>> '))
    phone_number = (input('Введите номер телефона: \n>>> '))
    file.write(first_name + ' '+ second_name + ' ' + phone_number + '\n')


def Find_text_in_data():
  with open('data.txt', 'r', encoding='utf-8') as file:
    book = file.read().split('\n')
    word = input('Введите слово для поиска: \n>>> ')
    for i in book:
      if word in i:
        print(f'Найдено: {i}')

def Delete_line(text):
  pattern = re.compile(re.escape(text))
  with open('data.txt', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
      result = pattern.search(line)
      if result is None:
        file.write(line)        
      file.truncate() 

def Replace_data(new_text, old_text):
  with open('data.txt', 'r') as file:
    old_data = file.read()
  new_data = old_data.replace(old_text, new_text)
  with open('data.txt', 'w') as file:
    file.write(new_data)

while True:
  print('Введите номер операции:')
  print('[0] - Поиск')
  print('[1] - Просмотр')
  print('[2] - Добавить текст в файл')
  print('[3] - Удалить запись из файла')
  print('[4] - Заменить информацию в файле')
  print('[5] - Выход')

  mode = input('>>>')
  if mode == '1':
    print(Show_data())
  elif mode == '0':
    Find_text_in_data()
  elif mode == '2':
    Add_line_in_data()
  elif mode == '3':
    name = input('Что необходимо удалить?: \n>>> ')
    Delete_line(name)
  elif mode == '4':
    old_text = input('Что необходимо переименовать?: \n>>> ')
    new_text = input('Введите новое название: \n>>> ')
    Replace_data(new_text, old_text)
  elif mode == '5':
    break
  else:
    print('No mode')