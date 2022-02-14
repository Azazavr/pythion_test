# Задание 1
"""
Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document выводит
на экран информацию о том, что редактирование документов недоступно для бесплатной версии. Создайте подкласс ProEditor,
 в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и, если он корректный,
 создайте экземпляр класса ProEditor, иначе Editor. Вызовите методы просмотра и редактирования документов. """

#Так, сегодня уже чуть лучше. В первый день вообще депресняк был, уже готов был всё бросать :)
#Тут точно можно доработать, вариант на скорую руку

class Editor:
    def __init__(self, passkey):
        self.passkey = passkey

    def checkkey(passkey):
        key = "01001"
        if passkey == key:
            ProEditor.edit_document(self=passkey)
        else:
            Editor.view_document(self=passkey)

    def view_document(self):
        print("Доступ только для просмотра")


class ProEditor:
    def edit_document(self):
        print("Редактируем документ")


try1 = Editor.checkkey("01001")

try2 = Editor.checkkey("10001")
