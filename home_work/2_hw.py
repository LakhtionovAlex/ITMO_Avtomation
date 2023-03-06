

def task_1():
    values = [1, 10.2, 'test', [1, 2, 3], True]
    for elem in range(len(values)):
        print(type(values[elem]))


task_1()


def task_1_2():
    values = [1, 10.2, 'test', [1, 2, 3], True]
    for elem in values:
        types = type(elem)
        print(types)


task_1_2()


def task_1_3():
    numbers: int = 1
    float_num: float = 10.2
    line: str = 'test'
    num_list: list = [1, 2, 3]
    truth: bool = True
    return type(numbers), type(float_num), \
        type(line), type(num_list), type(truth)


task_1_3()


# Это числа Фибоначчи задача номер 2
def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


task_2()


# Задача номер 3
def task_3(x: int) -> int:
    return pow(x, 2)


print(task_3(2))
