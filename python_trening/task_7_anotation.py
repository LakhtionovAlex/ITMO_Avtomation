a: int = 5
b: str = 'стрижка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))


def str_len(s: str = '') -> int:
    return len(s)


print(str_len('ljhalsgjba'))


def s_list(x: list, y: list) -> list:
    if len(x) > len(y):
        return x
    else:
        return y


print(s_list([1, 2, 3], [2, 3]))

# функция добавляет значение в список
def fun_append(x: list, y: str) -> list:
    x.append(y)
    return x


print(fun_append(['1', '2', '3'], '4'))

# функция складывает все значения списка
def sum_number(x: list) -> int:
    return sum(x)


print(sum_number([1, 2, 3, 4]))
