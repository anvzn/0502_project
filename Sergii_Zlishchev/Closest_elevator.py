def elevator(left, right, call):
    if abs(call - right) > abs(call - left):
        return "left"
    else:
        return "right"
