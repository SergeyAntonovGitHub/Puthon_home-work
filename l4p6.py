from itertools import count, cycle

print('Чтобы продолжить программу нажмите Enter, для выход нажмите - q')

for i in count(int(input('Введите число: '))):
    print(i, end='')
    exit = 'q'
    if input() == 'q':
        break


print('Чтобы продолжить программу нажмите Enter, для выход нажмите - q')

enter = input('Введите список через пробел: ').split()
iterate = cycle(enter)
exit = None

while exit != 'q':
    print(next(iterate), end='')
    exit = input()