class Car:
    def __init__(self, maker, model, colour, price):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price

        self.carlist = []

    def __str__(self):
        return f'{self.maker} {self.model} {self.colour} {self.price}'

    def add_car(self):
        self.carlist.append(self)

    def show_car(self):
        return self.carlist[0]

    def sell_car(self):
        self.carlist.remove(self)

car1 = Car("BMW", "320i", "White", "$15000")
Car.add_car(car1)
car2 = Car("Audi", "A4", "Pink", "$8700")
Car.add_car(car2)
car3 = Car("Mercedes", "Vito", "Yellow", "$18500")
Car.add_car(car3)
car4 = Car("ZAZ", "Slavuta", "Black", "$2000")
Car.add_car(car4)

print(Car.show_car(car4))


"""Что то я совсем туплю. Не могу понять, как это всё в кучу реализовать.
Каким образом удалять купленный автомобиль из списка? Пока всё в одном классе делаю, еще не доделал. Уже пересмотрел
 тонну уроков разных, и чем дальше в лес, тем толще партизаны"""


# Car.sell_car(car4)
#проверка на отсутствие объекта в списке...
# print(Car.show_car(car4))
# print(Car.show_car())

# print("""Выберите автомобиль для покупки:
#       1. "BMW", "320i"
#       2. "Audi", "A4"
#       3. "Mercedes", "Vito"
#       4. "ZAZ", "Slavuta""")
#
# choice = input()
#
# if choice == 1:
#     Car.buy_car(0)
# elif choice == 2:
#     Car.buy_car(1)
# elif choice == 3:
#     Car.buy_car(2)
# elif choice == 4:
#     Car.buy_car(3)
