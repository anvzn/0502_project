# Binary Representation of an Integer
modified_bin_positive = []
modified_bin_negative = []
def showBits(n):
    modified_bin_positive.clear()
    modified_bin_negative.clear()
    if n == 0:
        return [0] * 32
    if n > 0:
        positive_list = [0] * 32
        len_positive_bin = len(bin(n)) - 2
        a = 0
        b = 1
        for c in bin(n)[2:]:
            if c == '1':
                modified_bin_positive.append(b)
            if c == '0':
                modified_bin_positive.append(a)
        positive_list_modified = positive_list[:-len_positive_bin] + modified_bin_positive
        return positive_list_modified
    if n < 0:
        negative_list = [1] * 32
        len_negative_bin = len(bin(n)) - 3
        b = 0
        c = 1
        for d in bin(n)[3:]:
            if d == '1':
                modified_bin_negative.append(b)
            if d == '0':
                modified_bin_negative.append(c)
        negative_list_modified = negative_list[:-len_negative_bin] + modified_bin_negative[:-1] + [1]
        return negative_list_modified

print(showBits(701))
print(showBits(-245))
print(showBits(12336))
print(showBits(1))
print(showBits(-1))
