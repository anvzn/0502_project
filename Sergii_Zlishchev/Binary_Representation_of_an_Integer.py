def showBits(n):
    result_list_1 = []
    result_list_2 = []
    m = 31
    a = 32
    d = n
    while a > 0:
        if n >= 0:
            if (2 ** m) > n:
                result_list_1.append(0)
                a -= 1
                m -= 1
            else:
                b = bin(n)
                b = b[2:]
                for i in b:
                    i = int(i)
                    result_list_2.append(i)
                break
# Wrong implementation for negative value
        else:git
            if (2 ** m) > abs(n):
                result_list_1.append(1)
                a -= 1
                m -= 1
            else:
                b = bin(n)
                b = b[3:]
                for i in b:
                    i = int(i)
                    result_list_2.append(i)
                break

    return (result_list_1 + result_list_2)