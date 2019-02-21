str = 'hi hi what is your name my name is bond james bond my name is damme van damme claude van damme jean claude van damme'

l1 = str.split()
l2 = []
s1 = set(l1)
for i in s1:
    t1 = (l1.count(i), i)
    l2.append(t1)

l2.sort(key=lambda tup: (-tup[0], tup[1]))

for i in l2:
    print(i[1])
