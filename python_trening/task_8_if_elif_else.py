# num_flout = 3.4
#
# if num_flout > 0:
#     print('Положительное число')
# elif num_flout == 0:
#     print('Ноль')
# else:
#     print('Число отрицательное')
#
#
# permit_print = True
#
# if num_flout> 0 and permit_print:
#     print('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')

num = int(input())

if num > 0 and num <= 4:
    print('бакалавр')
elif num >= 5 and num <= 6:
    print('магистр')
elif num >= 7 and num <= 9:
    print('аспирант')
else:
    print('Введите корректный год обучения')


