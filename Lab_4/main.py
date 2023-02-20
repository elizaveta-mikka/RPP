import os
from pathlib import Path
import csv


def gen(self):
    for i in self.__dict__:
        yield self.__dict__[str(i)]


def compare1(item):
    return dict2[item][3]


def compare2(item):
    return dict2[item][4]


def list_output(self, lst, col):
    k = 0
    s = ""
    for i in lst:
        for j in col:
            s += str(j) + ' - ' + str(self.__dict__[str(i)][k]) + '; '
            k += 1
        print(s)
        s = ""
        k = 0


def add(self, col, n):
    add_list = []
    for i in col:
        print("Введите " + i + ":")
        add_list.append(input())
    with open("data.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(add_list)
    csvfile.close()
    my_dict.__setattr__(n, add_list)

class Dict:

    def __setattr__(self, key, value):
        self.__dict__[str(key)] = value

    def __iter__(self):
        self.n = len(self.__dict__)
        self.k = 0
        return self

    def __getitem__(self, item):
        self.n = len(self.__dict__)
        if item < self.n:
            return self.__dict__[item]

    def __next__(self):
        if self.k < self.n:
            nx = self.__dict__[str(self.k)]
            self.k += 1
            return nx


class Ex_Dict(Dict):

    @staticmethod
    def copy(self):
        dct = {}
        lst = []
        for i in self.__dict__:
            for j in range(5):
                if 1 < j < 4:
                    lst.append(self.__dict__[i][j])
                else:
                    lst.append(int(self.__dict__[i][j]))
            dct[int(i)] = lst
            lst = []
        return dct

    @staticmethod
    def select(self):
        lst = []
        for i in self.__dict__:
            if int(self.__dict__[i][4]) > 4:
                lst.append(int(i))
        return lst

    def __repr__(self):
        return f"{self.__class__}:{self.__dict__}"

    def __str__(self):
        return f"{self.__dict__}"


my_list = []
n = 0
my_dict = Ex_Dict()
col = ['№ поста', '№ комментария', 'Дата и время', 'Текст комментария', 'Лайки']
path = Path(Path.home(), "Desktop", "Directory")
print("Количество файлов в директории Directory - " + str(len(os.listdir(path))))
with open("data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        my_list = []
        for p in col:
            my_list.append(row[p])
        my_dict.__setattr__(n, my_list)
        n += 1
print("Сортировка по строковому полю (Текст комментария):")
dict2 = Ex_Dict.copy(my_dict)
sorted_keys_1 = sorted(dict2, key=compare1)
list_output(my_dict, sorted_keys_1, col)
print("Сортировка по числовому полю (Лайки):")
sorted_keys_2 = sorted(dict2, key=compare2)
list_output(my_dict, sorted_keys_2, col)
print("Критерий для выборки - количество лайков не менее 5:")
select_keys = Ex_Dict.select(my_dict)
list_output(my_dict, select_keys, col)
it = iter(my_dict)
print(next(it))
print(next(it))
print("Хотите ввнести новые записи в файл?\n1.Да")
an = input()
if an == 1:
    add(my_dict, col, n)


