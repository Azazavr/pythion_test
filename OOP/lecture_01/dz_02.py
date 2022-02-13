#Задание 2

"""Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""

class Books:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'{self.author}, {self.name}, {self.year}, {self.genre}'

    #не мой код. Работает вроде, но мне непонятно, зачем переопределять метод
    # def __eq__(self, other):
    #     if isinstance(other, Books):
    #         return (
    #                 self.author == other.author and self.name == other.name and
    #                 self.year == other.year and self.genre == other.genre
    #         )

    #Мне понятнее такой вариант сравнения:
    def __eq__(self, other):
        if self.author == other.author and self.name == other.name and self.year == other.year and \
                self.genre == other.genre:
            return True
        else:
            return False

    def load_references(self):
        return BookReview()

    def add_review(self, comments):
        self.book_review = self.load_references()
        self.book_review.add_review(comments)

    def open_review(self):
        return self.book_review.read_review()


class BookReview:
    reviews = list()

    def __init__(self):
        pass

    def add_review(self, review):
        return self.reviews.append(review)

    def read_review(self):
        return self.reviews

    #код взят из урока. Не понимаю принцип, как он в цикле достаёт всё из списка (хотя мы этот метод не вызываем)
    # def read_review_elem(self, i):
    #     return self.reviews[i]

    def __str__(self):
        return f"ref: {self.reviews}"


book_one = Books(author="Уильям Шекспир", name="Гамлет", year=2011, genre="Классика")
book_two = Books(author="Максим Горький", name="На дне", year=2016, genre="Драма")
book_three = Books(author="Братья Гримм", name="Сказки", year=2016, genre="Детские")
book_four = Books(author="Уильям Шекспир", name="Гамлет", year=2011, genre="Классика")

print(book_two)

print('Comments for this book:')
book_two.add_review('норм')
book_two.add_review('жирок')
book_two.add_review('я-бы лучше написал')
print('*********************')
print(book_two.open_review())

print(book_one == book_two)
print(book_one == book_four)
