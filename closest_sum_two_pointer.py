from typing import List

def get_closest_vals(array1: List, array2: List, x: int) -> List:
    diff = float('inf')
    closest_pair = []
    pointer_1 = 0
    pointer_2 = len(array2) - 1
    while pointer_1 < len(array1) and pointer_2 >= 0:
        element1 = array1[pointer_1]
        element2 = array2[pointer_2]
        current_diff = abs((element1 + element2) - x)
        if element1 + element2 == x:
            closest_pair = [element1, element2]
            return closest_pair
        if element1 + element2 < x:
            pointer_1 += 1
            if current_diff < diff:
                diff = current_diff
                closest_pair = [element1, element2]
        elif element1 + element2 > x:
            pointer_2 -= 1
            if current_diff < diff:
                diff = current_diff
                closest_pair = [element1, element2]

    return closest_pair


print(get_closest_vals([1, 4, 5, 7], [10, 20, 30, 40], 50))