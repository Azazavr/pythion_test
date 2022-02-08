class books:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def get_author(self):
        return self.author

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

book_one = books(author="Уильям Шекспир", name="Гамлет", year=2011, genre="Классика")
book_two = books(author="Максим Горький", name="На дне", year=2016, genre="Драма")
book_three = books(author="Братья Гримм", name="Сказки", year=2016, genre="Детские")
