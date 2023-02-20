import math

# В каждом классе есть два метода с идентичными названиями. Но несмотря на то, что называются они одинаково,
# действуют по разному. Это и есть проявление полиморфизма.
class Square:  # Класс - Квадрат

    def __init__(self, a):
        self.a = a

    def find_s(self):
        return self.a ** 2

    def info(self):
        print("Все стороны этой геометрической фигуры равны " + str(self.a))


class Circle:  # Класс - Круг

    def __init__(self, r):
        self.r = r

    def find_s(self):
        return math.pi * (self.r ** 2)

    def info(self):
        print("Радиус этой фигуры равен " + str(self.r))


class Triangle:  # Класс - Треугольник

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_s(self):
        p = (self.a + self.b + self.c)/2
        s = p*(p-self.a)*(p-self.b)*(p-self.c)
        return math.sqrt(s)

    def info(self):
        print("Стороны этой фигуры равны " + str(self.a) + ', ' + str(self.b) + ', ' + str(self.c))


fig1 = Triangle(4, 11, 12)
fig2 = Circle(8)
fig3 = Circle(9)
fig4 = Square(5)
fig5 = Square(11)
figures = [fig1, fig2, fig3, fig4, fig5]  # В коллекцию записываются все созданные фигуры,
# они являются экземплярами разных классов, с одинаковыми методами.
for i in figures: # В зависимости от того экземпляр какого класса представлен, вызываются соответствующие
    # методы данного класса.
    i.info()
    print("Площадь этой фигуры равна " + str(i.find_s()))
