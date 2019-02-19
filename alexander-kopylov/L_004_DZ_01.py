# Closest elevator
def elevator(left, right, call):
    left_distance = abs(call - left)
    right_distance = abs(call - right)
    if left_distance < right_distance:
        return "left"
    if right_distance < left_distance:
        return "right"
    if left_distance == right_distance:
        return "right"

