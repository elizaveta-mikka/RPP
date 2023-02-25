import math


# В каждом классе есть два метода с идентичными названиями. Но несмотря на то, что называются они одинаково,
# действуют по разному. Это и есть проявление полиморфизма.
class Figures:
    @staticmethod
    def figure_info():
        s = "Данная геометрическая фигура - "
        return s


class Square(Figures):  # Класс - Квадрат

    def __init__(self, a):
        self.a = a

    def find_s(self):
        return self.a ** 2

    @staticmethod
    def get_name():
        name = "квадрат"
        return name


class Circle(Figures):  # Класс - Круг

    def __init__(self, r):
        self.r = r

    def find_s(self):
        return math.pi * (self.r ** 2)

    @staticmethod
    def get_name():
        name = "круг"
        return name


class Triangle(Figures):  # Класс - Треугольник

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_s(self):
        p = (self.a + self.b + self.c) / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(s)

    @staticmethod
    def get_name():
        name = "треугольник"
        return name


fig1 = Triangle(4, 11, 12)
fig2 = Circle(8)
fig3 = Circle(9)
fig4 = Square(5)
fig5 = Square(11)
figures = [fig1, fig2, fig3, fig4, fig5]  # В коллекцию записываются все созданные фигуры,
# они являются экземплярами разных классов, с одинаковыми методами.
for i in figures:  # В зависимости от того экземпляр какого класса представлен, вызываются соответствующие
    # методы данного класса.
    info_fig = i.figure_info() + i.get_name()
    print(info_fig)
    print("Площадь этой фигуры равна " + str(i.find_s()))
