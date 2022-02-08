a = range(1, 5)
print(*a)


def test(args):
    for arg in args:
        print("arg #", arg)


test([1, 2, 3, 4])

#квадрат для диапазона чисел
b = [x ** 2 for x in range(1, 5)]
print(b)

#простой ренератор словаря
b = {x: x ** 2 for x in range(1, 5)}
print(b)
