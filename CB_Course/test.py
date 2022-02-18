




# from tkinter import *
#
#
# class Rectangle:
#     def __init__(self):
#         pass
#
#     def insert_rectangle(self):
#         self.e1.insert(0, "рисуем квадрат")
#     #где то тут зарыт косяк, который я пока не могу понять. Что должно приходить в self?
#
#
# root = Tk()
# but = Button(text="Квадрат", command=Rectangle.insert_rectangle())
# e1 = Entry(width=50)
# e1.pack()
# but.pack()
# root.mainloop()



# from tkinter import *
#
# clicks = 0
#
#
# class Rectangle:
#     def __init__(self):
#         pass
#
#
# def click_button():
#     l1 = Label(text="Текст под кнопкой", font="Arial 16")
#     l1.pack()
#
#
# root = Tk()
# root.title("Окно :)")
# root.geometry("400x300+300+200")
# btn = Button(text="Кнопка", bg='#d7d8e0', bd=0, command=click_button())
# btn.pack()
# root.mainloop()


# from tkinter import *
#
# clicks = 0
#
#
# def click_button():
#     global clicks
#     clicks += 1
#     btn.config(text="Clicks {}".format(clicks))
#
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")
#
# btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
#              padx="20", pady="8", font="16", command=click_button)
# btn.pack()
#
# root.mainloop()




# import tkinter as tk
#
#
# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self.init_main()
#
#     def init_main(self):
#         btn_open_dialog = tk.Button(text="Кнопочка", command=self.open_dialog(), bg='#d7d8e0', bd=0,
#                                     compound=tk.TOP)
#         btn_open_dialog.pack(side=tk.TOP)
#
#     def open_dialog(self):
#         pass
#
#
# class Child(tk.Toplevel):
#     def __init__(self):
#         super().__init__(root)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Main(root)
#     app.pack()
#     root.title("Button test")
#     root.geometry("650x450+300+200")
#     root.resizable(False, False)
#     root.mainloop()




# class Car:
#
#     def __init__(self,name, years_old, price):
#
#         self.years_old = years_old
#         self.price = price
#         self.name = name
#
#     def __str__(self):
#         return f' {self.name}, {self.years_old}, {self.price}'
#
#
# class Car_store:
#     list = []
#
#     def addAuto_to_list(self, *q):
#         self.list.extend(*q)
#
#
#
# class Seller:
#     def suggest(self):
#         for i in self.list:
#             print('купи машину : ' , i)
#
# mercedes = Car('мерс',60, 200000)
#
# djiga = Car('жига', 100, 23)
#
# store = Car_store()
# store.addAuto_to_list((mercedes, djiga))
# almost_sold = Seller()
# Seller.suggest(store)





# Решение Вадима
# def murzilka(n):
#     massiv = []
#     for i in range(2, n+1):
#         if i == 2:
#             massiv.append(i)
#         if i>2 :
#             for j in massiv :
#                 if i % j == 0:
#                     break
#                 if j == massiv[-1] :
#                     massiv.append(i)
#
#     print(massiv)
#
# murzilka(23)


# a = int(input("Введите размер списка:  "))
# spisok_chisel = []
# while a != 0:
#     spisok_chisel.append(input("Введите элементы "))
#     a -= 1
#
# print(spisok_chisel[::-1])


# def prostoe(k):
#     temp = 0
#     for i in range(2, k // 2 + 1):
#         if k % i == 0:
#             temp = temp + 1
#     if temp <= 0:
#         return k
#     else:
#         return 0
#
# a = int(input("Введите число:  "))
# spisok_chisel = [] #иду по простому. Сначала список всех чисел, а потом перебор этого списка
# result = [] #сюда складываю результат проверки на простость :)
#
# if a <= 1:
#     print("В общем на этом всё :)")
#
# else:
#     for i in range(a):
#         if i+1 != 1:
#             spisok_chisel.append(i+1)
#
#     for i in range(len(spisok_chisel)):
#         if prostoe(spisok_chisel[i]) != 0:
#             result.append(spisok_chisel[i])
#
#     print(result)
#
# print("""Выберете операцию, которую хотите произвести с результатами:
#       1. Сложение
#       2. Умножение
#       3. Выход
#       """)
# choice = int(input())
# tempo = 1
# if choice == 1:
#     print(sum(result))
# elif choice == 2:
#     for i in range(len(result)):
#         tempo *= result[i]
#     print(tempo)
# elif choice == 3:
#     exit(0)



# new_list = []
# a = int(input("Введите простое число для получения списка сумм его элементов:  "))
# result = []
# b = 0
# for i in range(a):
#     new_list.append(i+1)
#
# for i in range(len(new_list)):
#     b += new_list[i]
#     result.append(b)
#
# print(result)

# summ = 0
# for i in [1, 2, 3, 4, 5]:
#     summ += i
# print(summ)


# a = 4
# b = 0
#
# while a:
#     b += a
#     a -= 1
#
# print(b)


# new_list = [1, 2, 3, 4, int(input("Введите число для добавления в список:  "))]
#
# new_list.sort()
#
# print("Минимальное значение", new_list[0])
# print("Максимальное значение", new_list[-1])
# summa = 0
# for i in range(len(new_list)):
#     summa += new_list[i]
#
# print("Сумма элементов списка", summa)
# print("Среднее значение", int(summa / len(new_list)))



# import random
# n = None
#
#
# def get_list(n):
#     user_list = []
#     for i in range(n):
#         user_list.append(random.randint(0, 100))
#     print("Old list : {} \n".format(user_list), end="")
#     new_list = user_list[:]
#     print("new list : {}".format(new_list[::-1]), end="")
#     power = int(input("\n vvedi pow"))
#     for i in user_list:
#         print("{} = {}".format(i, i ** power))
#
# get_list(10)





# my_list = [1, 3, 4, 6, 34, 23, 32, 543, 434, 12]
#
# # print(my_list.sort())
# my_list.sort(reverse=True)
# print(my_list)
#
# a = int(input("Введите число:  "))
#
# for i in range(len(my_list)):
#     print(my_list[i] ** a)



# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n - 1) * n
#
#
# print(fac(5))

# a = "hello"
#
# def test(*text):
#     for i in text:
#         print(i, ' ')
#     print(text, len(text))
#
#
# test(a)
# def fac(n):
#     if n == 0:
#         return 1
#     # print(fac(n - 1) * n)
#     return fac(n - 1) * n #4*5=3*20=2*60=1*120
#
#
# print(fac(5))



# def faktor(x):
#     if x <= 0:
#         return 1
#     else:
#         return x + faktor(x-1)
# #толстые пальцы, не тот знак поставил видимо :) (на самом деле перепутал)
#
#
# print(faktor(2)-1)



# def stupe(n):
#     if n in (1, 2):
#         return n
#
#     print(f"{n}-1 + {n}-2 =", n - 1 + n - 2, f'n={n}', f'n-1={n-1}', f'n-2={n-2}')
#     return stupe(n - 1) + stupe(n - 2)  #4(3(2(2)+ 1(1)) 2) 3 3 1
#
#
# print(stupe(5), "способами можно подняться на заданную ступеньку")
#
#
#
# def stupeni(x):
#     if x <= 2:
#         return x
#     else:
#         return stupeni(x - 1) + stupeni(x - 2)
#
# print(stupeni(5))

# def recursive(a=6, b=10):
#     if a == b:
#         return b
#     return b+recursive(a, b - 1)#какие ещё варианты решения этой задачи есть
#
#
# print(recursive())


# def faktor(x):
#     if x <= 0:
#         return 1
#     else:
#         return (x + faktor(x-1))
#
# print(faktor(2)-1)

# a = 10
# b = 0
#
# while a:
#     b += a
#     a -= 1
#
# print(b)


# def test(text):
#     reversed_text = text[::-1]
#     temp_test = ""
#
#     for i in range(len(text)):
#         if text[i] == reversed_text[i]:
#             temp_test = True
#         else:
#             temp_test = False
#             break
#     return temp_test
#
#
# print(test("роза упала на лапу азор"))


# def is_palindrome(word):
#     return word == word[::-1]
#
# print(is_palindrome("роза упала на лапу азор"))

# a = "abba"
# b = a[::-1]
# c = ''
# for i in range(len(b)):
#     if a[i] == b[i]:
#         c = True
#
#     else:
#         c = False
#
# print(c)


# НУ КАК ТАК_ТО???

# def recursive(x):
#     print(x)
#     if x < 4:
#         recursive(x + 1)
#     print(x)
#
#
# recursive(1)



# def faktor(x):
#     if x <= 0:
#         return 1
#     else:
#         return x * faktor(x-1)
#
#
# print(faktor(6))





# #Блин, по моему я как то всё сложно и громоздко решаю :(
#
# def is_palindrom(stroka):
#     first = list(stroka)
#     second = list(stroka)
#     second.reverse()
#     test = ""
#     for i in range(len(stroka)):
#         if first[i] == second[i]:
#             test = "Слово палиндром"
#         else:
#             test = "Слово НЕ палиндром"
#             break
#     return test
#
# print(is_palindrom("ABWBA"))

# def stepen_dvoiki(a):
#     if (a / 2) % 2 != 0:
#         return "No"
#     elif:
#         a / 2






# #Сложение
# def plus_menu(x, y):
#     return (x + y)
#
#
# #Умножение
# def multiply_menu(x, y):
#     return (x * y)
#
#
# for i in range(21):
#     print("Результат сложения: ", plus_menu(-5, i/2))

# for i in range(21):
#     print("Результат умножения: ", multiply_menu(-5, i/2))




# #не совсем понял условие. Нужно 2 функции - основная с запросом и которая производит вычисления?
#
#
# def srednee(a, b, c):
#     # return int((a + b + c)/3)
#     return (a + b + c)/3
#
#
# def main():
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     c = int(input("Введите третье число: "))
#     return srednee(a, b, c)
#
#
# print(main())



# #Сложение
# def plus_menu(x, y):
#     return print("Результат: ", x + y)
#
#
# #Вычитание
# def minus_menu(x, y):
#     return print("Результат: ", x - y)
#
#
# #Деление
# def division_menu(x, y):
#     if y != 0:
#         return print("Результат: ", x / y)
#     else:
#         return print("Деление на 0")
#
#
# #Умножение
# def multiply_menu(x, y):
#     print("Результат: ", x * y)
#
#
# z = 0
# while z != 5:
#     z = int(input("""Введите требуемую операцию\n
#         1. Сложение
#         2. Вычитание
#         3. Деление
#         4. Умножение
#         5. Выход
#             """))
#     if 5 <= z <= 1:
#         x = int(input("Введите первое число: "))
#         y = int(input("Введите второе число: "))
#
#         if z == 1:
#             plus_menu(x, y)
#
#         elif z == 2:
#             minus_menu(x, y)
#
#         elif z == 3:
#             division_menu(x, y)
#
#         elif z == 4:
#             multiply_menu(x, y)
#
#     elif z == 5:
#         print("Выход из приложения")
#
#     else:
#         print('Некорректный ввод')
#



#
# import math
# x = int(input("Введите любое число: "))
# y = int(input("""Введите требуемую операцию\n
#     1. Сложение
#     2. Вычитание
#     3. Деление
#     4. Возведение в степень
#     5. Синус
#     6. Косинус
#     7. Тангенс
# """))
# if y == 5 or y == 6 or y == 7:
#     if y == 5:
#         print(math.sin(x))
#     elif y == 6:
#         print(math.cos(x))
#     elif y == 7:
#         print(math.tan(x))
# else:
#     if y == 1:
#         z = int(input("Введите второе число для суммирования и нажмите ENTER: "))
#         print(x + z)
#     elif y == 2:
#         z = int(input("Введите второе число для вычитания и нажмите ENTER: "))
#         print(x - z)
#     elif y == 3:
#         z = int(input("Введите второе число для деления и нажмите ENTER: "))
#         if z == 0:
#             print("На ноль делить нельзя")
#         else:
#             print(x / z)
#     elif y == 4:
#         z = int(input("Введите степень, в которую вы хотите возвести ваше число и нажмите ENTER: "))
#         print(pow(x, z))


# x = int(input("введите X = "))
# y = int(input("введите Y = "))
# for i in range(x):
#     for j in range(y):
#         if j <= i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
# input()


# Создайте функцию, которая выводит приветствие для пользователя с заданным именем.
# Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.
# def say_name(name):
#     if name == "":
#         return print("Привет, Юрец")
#     else:
#         return print("Привет, ", name)
#
# say_name("User_name")


# рисуем квадрат
# x = int(input("Введите сторону квадрата: "))
#
# for i in range(x):
#     for j in range(x):
#         print("*", end='')
#     print()


# прямоугольный треугольник заданной высоты

# x = int(input("Введите сторону треугольника: "))
#
# for i in range(x):
#     for j in range(i+1):
#         print("*", end='')
#     print("")


# x = int(input("Введите число, факториал которого нужно вычислить: "))
# z = x
# count = 1
# while z != 1:
#     x *= count
#     count += 1
#     z -= 1
#
# print(x)