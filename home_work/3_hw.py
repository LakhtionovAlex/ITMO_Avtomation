# задача 3
def max_number(num_1, num_2):
    return max(num_1, num_2)


# задача 4
def different_number(num_1, num_2):
    total_num = num_1 - num_2
    if abs(total_num) == 135:
        print('yes')
    else:
        print('No')


# задача 5
def season_year(month):
    winter, spring, summer, autumn = [12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]
    if month in winter:
        print('зима')
    elif month in spring:
        print('весна')
    elif month in summer:
        print('лето')
    elif month in autumn:
        print('осень')
    else:
        print('Введите корректный номер месяца!')


# задача 6
def check_more_10(num_1, num_2, num_3):
    list_num = [num_1, num_2, num_3]
    count = 0
    for number in list_num:
        if number >= 10:
            count += 1
    if count == 3:
        print('yes')
    else:
        print('no')


# задача 7
def count_positive_numbers(list_number: list):
    count = 0
    for number in list_number:
        if number >= 0:
            count += 1
    print(count)


# задача 8
def count_days(years, month):
    total_days = years * 348 + month * 29
    print(total_days)


count_days(int(input('Введите количество лет: ')), int(input('Ведите количество месяцев: ')))
