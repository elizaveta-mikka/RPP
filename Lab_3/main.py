import os
from pathlib import Path
import csv


def compare1(item):
    return my_dict[item][3]


def compare2(item):
    return int(my_dict[item][4])


def list_output(list):
    for i in list:
        print('№ поста - ' + str(my_dict[i][0]) + '; № комментария - ' + str(my_dict[i][1]) + '; Дата и время - '
              + str(my_dict[i][2]) + '; Текст комментария - ' + str(my_dict[i][3]) + '; Лайки - ' + str(my_dict[i][4]),
              end='\n')


path = Path(Path.home(), "Desktop", "Directory")
print("Количество файлов в директории Directory - " + str(len(os.listdir(path))))
my_dict = {}
k = 0
with open("data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        my_dict[k] = [row['№ поста'], row['№ комментария'], row['Дата и время'], row['Текст комментария'], row['Лайки']]
        k += 1
print("Сортировка по строковому полю (Текст комментария):")
sorted_keys_1 = sorted(my_dict, key=compare1)
list_output(sorted_keys_1)
sorted_keys_2 = sorted(my_dict, key=compare2)
print("Сортировка по числовому полю (Лайки):")
list_output(sorted_keys_2)
print("Критерий для выборки - количество лайков не менее 5:")
select_keys = []
for i in my_dict:
    if int(my_dict[i][4]) > 4:
        select_keys.append(i)
list_output(select_keys)
print("Добавление новых элементов в файл")
add_list = []
print("Введите № поста:")
add_list.append(input())
print("Введите № комментария:")
add_list.append(input())
print("Введите дату и время:")
add_list.append(input())
print("Введите текст комментария:")
add_list.append(input())
print("Введите количество лайков:")
add_list.append(input())
with open("data.csv", "a", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(add_list)
csvfile.close()
