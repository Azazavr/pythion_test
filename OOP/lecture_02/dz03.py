class A:
    def __init__(self):
        print("Запускается класс A")

    def sub_method(self, b):
        print('метод класса А', b)


class B(A):
    def __init__(self):
        print("Запускается класс B")
        super().__init__()

    def sub_method(self, b):
        print('метод класса В', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print("Запускается класс C")
        super().__init__()

    def sub_method(self, b):
        print("метод класса С", b)
        super().sub_method(b + 1)


class D(C):
    def __init__(self):
        print("Запускается класс D")
        super(C, self).__init__()

    def sub_method(self, b):
        print("метод класса D", b)
        super().sub_method(b + 1)


c = C()
c.sub_method(1)

d = D()
d.sub_method(2)
#Основано на примере из урока. Но немного взрывает мозг. Надо привыкнуть
