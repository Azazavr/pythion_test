a = range(1, 5)
print(*a)


def test(args):
    for arg in args:
        print("arg #", arg)


test([1, 2, 3, 4])
