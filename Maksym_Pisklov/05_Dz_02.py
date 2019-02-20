s = '1 2 2 2 3 4 5 9 7 10 f 10 7 3 1 2 4'

s_int = [int(i) for i in s if '0' <= i <= '9']

new_set = set()

for i in s_int:
    if i in new_set:
        print("Yes")
    else:
        print("No")
        new_set.add(i)

