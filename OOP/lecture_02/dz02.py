class Figures:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figures):

    def get_rectangle(self):
        return print("Rectangle")

    def press_button(self):
        print('Button pressed')


r1 = Rectangle(1, 2)
r1.press_button()

#или тут нужно было подключать библиотеку и прописать вызов функции BUTTON_PRESSED (или как то так)?
