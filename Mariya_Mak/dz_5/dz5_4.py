str = "ivanov paper 10 petrov pen 5 ivanov marker 3 ivanov paper 7 petrov envelope 20 ivanov envelope 5"
l1 = str.split()
dic1 = {}
s_of_users = set()
for i in range(0, len(l1), 3):
    s_of_users.add(l1[i])

l2 = list(s_of_users)
l2.sort()
dic1 = dict.fromkeys(l2)

d_k = dic1.keys()

for i in range(0, len(l1), 3):
    if l1[i] in d_k:
       key_with_item = dic1.get(l1[i])
       if isinstance(key_with_item, dict):
           key_with_count = key_with_item.get(l1[i + 1])
           if isinstance(key_with_count, int):
               key_with_item[l1[i + 1]] = key_with_count + int(l1[i + 2])
           else:
               key_with_item[l1[i + 1]] = int(l1[i + 2])
       else:
           dic1[l1[i]] = {l1[i + 1]: int(l1[i+2])}

dic2 = sorted(dic1.items(), key=lambda x: x[1])


print()