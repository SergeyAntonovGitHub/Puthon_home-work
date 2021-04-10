num_enter = (int(input("Введите число ")))
maximum = num_enter % 10
num = num_enter

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
    if digit == 9:
        break
    num = num // 10
    print(num)

print(f"Наибольшая цифра в числе {num_enter} = равана {maximum}")
