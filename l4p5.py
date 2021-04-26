from functools import reduce


def spisok(num_1, num_2):
    return num_1 * num_2


my_gen = [i for i in range(100, 1001, 2)]
print(f'Результат\n{reduce(spisok, my_gen)}')