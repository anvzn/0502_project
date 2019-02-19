# Sum of a nested list
def sum_nested(lst):
    new_list = []
    list_converter(lst, new_list)
    return sum(new_list)
def list_converter(lst, new_list):
    for a in lst:
        if isinstance(a, list):
            list_converter(a, new_list)
        else:
            new_list.append(a)

print(sum_nested(([[[[[1, 2, 2, 4]]]]], 4)))