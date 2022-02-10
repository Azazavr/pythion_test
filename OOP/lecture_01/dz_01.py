class Books:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'{self.author}, {self.name}, {self.year}, {self.genre}'

    def __eq__(self, other):
        if isinstance(other, Books):
            return (
                self.author == other.author and self.name == other.name and
                self.year == other.year and self.genre == other.genre
            )

    def get_author(self):
        return self.author

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre


book_one = Books(author="Уильям Шекспир", name="Гамлет", year=2011, genre="Классика")
book_two = Books(author="Максим Горький", name="На дне", year=2016, genre="Драма")
book_three = Books(author="Братья Гримм", name="Сказки", year=2016, genre="Детские")
book_four = Books(author="Уильям Шекспир", name="Гамлет", year=2011, genre="Классика")

print(book_one == book_two)
print(book_one == book_four)
print(book_one.get_genre())
