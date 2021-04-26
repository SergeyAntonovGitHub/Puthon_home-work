from itertools import count
from math import factorial

def fact_generate(number):
    fact_number = 1
    if number == 0:
        yield f'{number} = 1'
    for i in range(1, number + 1):
        fact_number *= i
        yield f'{i} = {fact_number}'

for arg in fact_generate(int(input('Введите число - '))):
    print('Факториал вашего числа = ')
    print(arg)