cortege = []
parameters = {'Название': '', 'Цена': '', 'Колличество': '', 'Ед. измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Колличество': [], 'Ед. измерения': []}
item_Number = 0

print('=' * 150)
while True:
    if input('Чтобы войти в программу - нажмите Enter, Для выхода - Введите ESC ').upper() == 'ESC':
        break
    item_Number += 1
    for accept in parameters.keys():
        enter = input(f'Введите параметр {accept} -  ')
        parameters[accept] = int(enter) if accept == 'Цена' or accept == 'Колличество' else enter
        analytics[accept].append(parameters[accept])
    cortege.append((item_Number, parameters.copy()))
    print('{:>54}'.format('Структура товаров'))
    print('=' * 150)
    print(cortege)
    print('=' * 150)
    print('{:>50}'.format("Аналитика"))
    print('=' * 150)
    for key, value in analytics.items():
        print(f'{key}: {value}')
    print('=' * 150)