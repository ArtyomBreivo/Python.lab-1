#Найдите сумму отрицательных элементов списка.
#Найдите сумму элементов списка между двумя первыми нулями. Если
#двух нулей нет в списке, то выведите ноль.
import random
#numbers = [random.randint(-10, 20) for _ in range(8)]
numbers = [1, 2, 0, -4, 3, 5, -1, 0, 3]
negative_sum = 0
for num in numbers:
    if num < 0:
        negative_sum += num
first_zero_found = False
sum_between_zeros = 0
for num in numbers:
    if num == 0:
        if first_zero_found:
            break
        first_zero_found = True
    elif first_zero_found:
        sum_between_zeros += num
print(f"Сумма отрицательных элементов: {negative_sum}")
if first_zero_found:
    print(f"Сумма элементов между двумя первыми нулями: {sum_between_zeros}")
else:
    print("Двух нулей в списке не найдено, сумма равна 0.")
