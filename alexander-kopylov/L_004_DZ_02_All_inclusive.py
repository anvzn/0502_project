# All inclusive
import math
from functools import reduce

arr_modified_all_the_same = []
arr_modified_all_different = []
arr_modified_some_different = []
unique_items_in_strng_num = []
fact_of_unique_items_in_strng_num = []

def contain_all_rots(strng, arr):
    if len(strng) == 0 and len(arr) == 0:
        return bool(True)
    if len(strng) == 0 and len(arr) > 0:
        return bool(True)
    if len(strng) == 1 and strng in arr:
        return bool(True)
    if len(arr) == 0 and len(strng) != 0:
        return bool(False)
    number_of_comb = math.factorial(len(strng))
    strng_modified = list(set(strng))
    for c in strng_modified:
        unique_items_in_strng_num.append(strng.count(c))
    for d in unique_items_in_strng_num:
        fact_of_unique_items_in_strng_num.append(math.factorial(d))
    comb_with_repetitions = number_of_comb // reduce((lambda x, y: x * y), fact_of_unique_items_in_strng_num)
    if len(strng) > 1:
        if len(arr) < comb_with_repetitions:
            return bool(False)
        if len(arr) >= number_of_comb:
            if len(set(strng)) == 1:
                for a in arr:
                    if a == strng:
                        arr_modified_all_the_same.append(a)
                if len(arr_modified_all_the_same) >= number_of_comb:
                    return bool(True)
            if len(set(strng)) == len(strng):
                for b in arr:
                    if set(b) == set(strng):
                        arr_modified_all_different.append(b)
                if len(set(arr_modified_all_different)) == number_of_comb:
                    return bool(True)
            if 1 < len(set(strng)) < len(strng):
                for e in arr:
                    if set(e) == set(strng) and len(e) == len(strng):
                        arr_modified_some_different.append(e)
                if len(set(arr_modified_some_different)) == comb_with_repetitions:
                    return bool(True)
            else:
                return bool(False)


print(contain_all_rots("", []))
print(contain_all_rots("", ['1']))
print(contain_all_rots("1", ['1']))
print(contain_all_rots("1", []))
print(contain_all_rots("113", ['113', '131', '311', '311111', '4444', '213', '132', '0909', '131']))
print(contain_all_rots("123", ['321', '231', '312', '4444', '213', '132', '0909']))
