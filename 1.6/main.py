#В кортеже целых чисел найдите максимальный и минимальный элементы.
import random
def my_max(tuple):
    if len(tuple) == 0:
        raise ValueError("Кортеж пуст")
    max_element = tuple[0]
    for element in tuple:
        if element > max_element:
            max_element = element
    return max_element


def my_min(tuple):
    if len(tuple) == 0:
        raise ValueError("Кортеж пуст")
    min_element = tuple[0]
    for element in tuple:
        if element < min_element:
            min_element = element

    return min_element

my_tuple = tuple(random.randint(1, 10) for _ in range(5))
#my_tuple = (4, 7, 2, 9, 1, 0, -3, 6)
max_element = my_max(my_tuple)
min_element = my_min(my_tuple)
print(f"Максимальный элемент: {max_element}")
print(f"Минимальный элемент: {min_element}")


