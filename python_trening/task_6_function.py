def add(x, y):
    return x + y


print(add(1, 2))

print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))
print(arg(2, 2))
print(arg(2, 2, '1', 1))


def renge_arg(a, b, c, d):
    return a + '' + b + '' + c + '' + d


print(renge_arg('1', '2', '3', '4'))
print(renge_arg('1', '2', d='3', c='4'))
