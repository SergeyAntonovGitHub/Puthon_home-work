def my_func_sum():
    summa = 0
    while True:
        string = input('Введите Enter, чтобы продолжить или введите Esc, для выхода из программы').split()
        for enter in string:
            if enter == 'Esc':
                return summa
            else:
                try:
                    summa = (summa + int(enter))
                except ValueError:
                    print('Вы тввели неверное значение, чтобы пререзапустить программу введите Esc')
                print(f'Сумма введённых чисел равна - {summa}')

print(my_func_sum())