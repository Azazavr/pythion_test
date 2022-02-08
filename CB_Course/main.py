a = range(1, 5)
print(*a)

print("Что то еще")


def test(args):
    for arg in args:
        print("arg #", args)


test([1, 3, 5])
