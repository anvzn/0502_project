str = '1,5,8,6,7,4,5,4,3,2,1'
str_output = ''
l1 = []
for i in str:
    if i.isdigit():
        if i in l1:
            str_output += "Yes,"
        else:
            l1.append(i)
            str_output += "No,"

print(str_output[:-1])



