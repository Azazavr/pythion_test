def season(num_of_mounth):
    winter = [1, 2, 12]
    for num in range(12):
        #if num_of_mounth < 3 or num_of_mounth == 12:
        if num_of_mounth in winter:

            return f"{num_of_mounth} Сейчас зима"
        elif 2 < num_of_mounth < 6:
            return f"{num_of_mounth} Сейчас весна"
        elif 6 < num_of_mounth < 9:
            return f"{num_of_mounth} Сейчас лето"
        elif 9 < num_of_mounth < 12:
            return f"{num_of_mounth} Сейчас осень"

print(season(2))







# class Auto:
#     def __init__(self, power, price, sefety):
#         self.power = power
#         self.price = price
#         self.sefety = sefety
#
#     def info(self):
#         return f" Power{self.power}, Price {self.price}, Sefety {self.sefety}"
#
#
# class AutoSalone:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __str__(self):
#         lst = ["bmw", "audi", "toyota", "mersedes"]
#         return f"{lst}"
#
#     # def info(self):
#     #     return bmw, audi, toyota, mersedes
#
#
# def sell_auto():
#     print(AutoSalone.__str__(list))
#     bmw = Auto(500, "30k$", "7/10")
#     audi = Auto(400, "25k$", "8/10")
#     toyota = Auto(250, "20k$", "9/10")
#     mersedes = Auto(450, "30k$", "10/10")
#     print(f" bmw {bmw.info()},\n audi{audi.info()},\n toyota{toyota.info()},\n mersedes{mersedes.info()}")
#
#     text = input(" Choose one of them\n")
#     if text == "bmw":
#         print(f"You bought bmw, congrat! With stats {bmw.info()}")
#     elif text == "audi":
#         print(f"You bought audi, congrat! With stats {audi.info()}")
#     elif text == "toyota":
#         print(f"You bought toyota, congrat! With stats{toyota.info()}")
#     elif text == "mersedes":
#         print(f"You bought mersedes, congrat! With stats{mersedes.info()}")
#
#
#
#
# sell_auto()
# #print(type(s))