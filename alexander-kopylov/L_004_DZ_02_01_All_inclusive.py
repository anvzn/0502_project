# All inclusive

def contain_all_rots(strng, arr):
    rots_variations = []
    rots_variations_arr = []
    if len(strng) == 0 and len(arr) == 0:
        return True
    if len(strng) == 0 and len(arr) > 0:
        return True
    if len(strng) == 1 and strng in arr:
        return True
    if len(arr) == 0 and len(strng) != 0:
        return False
    if len(strng) > 1 and len(arr) != 0:
        strng_double = strng * 2
        rots_variations.append(strng)
        print(strng_double)
        for a, b in zip(range(1, len(strng)), range(1, len(strng))[::-1]):
            print(a, -b)
            print(strng_double[a:-b])
            rots_variations.append(strng_double[a:-b])
        print(rots_variations)
        for c in arr:
            if c in rots_variations:
                rots_variations_arr.append(c)
        print(rots_variations_arr)
        if set(rots_variations) == set(rots_variations_arr):
            return True
        else:
            return False


# print(contain_all_rots("ab", ["ab", "sjqb", "twZNsslC", "jqbs"]))