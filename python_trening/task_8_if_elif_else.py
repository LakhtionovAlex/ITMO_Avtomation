num_flot = 3.4

if num_flot > 0:
    print('Положительное число')
elif num_flot == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num_flot > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

num = int(input())


if 0 > num <= 4:
    print('бакалавр')
elif 5 >= num <= 6:
    print('магистр')
elif 7 >= num <= 9:
    print('аспирант')
else:
    print('Введите корректный год обучения')
