#Определить, сколько в числе четных цифр, а сколько нечетных.
#Число вводится с клавиатуры.
num = int(input("Введите число: "))
even_count = 0
odd_count = 0
num_str = str(num)
for digit in num_str:
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Четных цифр: {even_count}")
print(f"Нечетных цифр: {odd_count}")
