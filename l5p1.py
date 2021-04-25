with open('p1.txt', 'w', encoding='utf-8') as f:
    while True:
        stroka = input('Введите следующую строчку - ')
        f.write(f'{stroka}\n')
        if not stroka:
            break