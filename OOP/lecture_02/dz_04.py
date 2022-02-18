class Car:
    TYPE = "Автомобиль"

    def __init__(self, maker, model, colour):
        self.maker = maker
        self.model = model
        self.colour = colour

    def get_info(self):
        return f'{self.maker}, {self.model}, {self.model}'


class Bus(Car):
    TYPE = "Автобус"

    def __init__(self, maker, model, colour, seats):
        super().__init__(maker, model, colour)
        self.seats = seats

    def get_info(self):
        return f'{self.maker}, {self.model}, {self.model}, Посадочных мест - {self.seats}'


class Suv(Car):
    TYPE = "Внедорожник"

    def __init__(self, maker, model, colour, awd):
        super().__init__(maker, model, colour)
        self.awd = awd

    def get_info(self):
        return f'{self.maker}, {self.model}, {self.model}, Полный привод = {self.awd}'

car = Car("Audi", "A4", "white")
car1 = Bus("Scania", "T100", "yellow", 12)
car2 = Suv("BMW", "X5", "black", True)

print(car.get_info())
print(car1.get_info())
print(car2.get_info())
