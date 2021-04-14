def my_func(x, y):
    x, y = float(x), int(y)
    if x <= 0 or y >= 0:
        print('Введены не правильные значения! правильные значения при x > 0, y < 0')
    else:
        z = 1
        for off in range(abs(y)):
            z = (z * 1) / x
        return f'"x" в степени "y" равен - {z}'

print(my_func(int(input('Введит число > 0 - ')), int(input('Введите число < 0 - '))))