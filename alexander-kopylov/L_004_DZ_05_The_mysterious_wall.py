# -*- coding: utf-8 -*-
def build_a_wall(x=0, y=0):
    if type(x) != int or type(y) != int:
        return None
    if len(str(x)) == 0 or len(str(y)) == 0:
        return None
    if x < 0 or y < 0:
        return None
    if x == 0 or y == 0:
        return None
    if x * y > 10000:
        return "Naah, too much...here's my resignation."
    list_x = list(range(1, x + 1))
    brick = '■■|'
    wall = ''
    wall_one_column = ''
    if x == 1 and y == 1:
        return '■■'
    if x == 1 and y > 1:
        return (brick * y)[:-1]
    if x > 1 and y == 1:
        for a in list_x:
            if a % 2 == 1:
                wall_one_column += '\n■■'
            if a % 2 == 0:
                wall_one_column += '\n■|■'
        modified_wall_one_column = wall_one_column[1:]
        return modified_wall_one_column
    if x > 1 and y > 1:
        for b in list_x:
            if b % 2 == 1:
                odd_row = brick * y
                wall += "\n" + odd_row[:-1]
            if b % 2 == 0:
                even_row = brick * (y + 1)
                wall += "\n" + even_row[1:-2]
        modified_wall = wall[1:]
        return modified_wall

print(build_a_wall(5, 5))