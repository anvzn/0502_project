l1 = [i for i in range(1, 20, 2)]

l2 = [i for i in range(1, 10)]

the_same_el = set(l1).intersection(l2)

l_the_same_el = list(the_same_el)
l_the_same_el.sort()

print(l_the_same_el)

