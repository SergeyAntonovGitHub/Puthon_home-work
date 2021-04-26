from random import randint

spisok = [randint(0, 100) for num in range(20)]
my_gen = [i for i in spisok if spisok.count(i) == 1]
print(f'Список:\n{spisok}')
print(f'Уникальные вхождения в список:\n{my_gen}')