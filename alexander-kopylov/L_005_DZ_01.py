# Дан список чисел, который могут содержать до 100000 чисел
# каждый. Определите, сколько в нем встречается различных чисел.
from random import randrange, choice
rng_01 = range(100000)
lst_01_step_01 = [randrange(1, 77777) for a in rng_01]
lst_01_step_02 = [choice(lst_01_step_01) for b in lst_01_step_01]
set_01 = set(lst_01_step_02)
print(f'We have {len(set_01)} unique values in our list')

# Даны два списка чисел, которые могут содержать до 100000
# чисел каждый. Посчитайте, сколько чисел содержится
# одновременно как в первом списке, так и во втором.
lst_02_step_01 = [randrange(66666, 99999) for a in rng_01]
lst_02_step_02 = [choice(lst_02_step_01) for b in lst_02_step_01]
set_02 = set(lst_02_step_02)
sets_int = set_01.intersection(set_02)
print(f'The number of unique values that belong to both lists is: {len(sets_int)}')

# Даны два списка чисел, которые могут содержать до 10000
# чисел каждый. Выведите все числа, которые входят как в
# первый, так и во второй список в порядке возрастания.
lst_03 = list(sets_int)
lst_03_srtd = sorted(lst_03)
lst_03_srtd_prt = lst_03_srtd[:10]
print(f'The beginning of our sorted intersection list is: {lst_03_srtd_prt}...')

# Во входной строке записана последовательность чисел через
# пробел. Для каждого числа выведите слово YES (в отдельной
# строке), если это число ранее встречалось в
# последовательности или NO, если не встречалось.


def number_finder(strng):
    print(f"\nWe have a string with numbers: '{strng}'")
    print('We\'ll try to find repeating numbers by checking all of them one by one')
    list_04 = strng.split(' ')
    for e, d in zip(list_04, range(0, len(list_04) - 1)):
        if d == 0:
            print(e, 'NO')
        if d > 0:
            try:
                list_04.index(e, 0, d)
            except ValueError:
                print(e, 'NO')
            else:
                print(e, 'YES')


strng_01 = "134 2 34678 33 456 33 54 98 2 33 9"
number_finder(strng_01)
