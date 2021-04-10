enter = list(input('Введите число элиментов в списке '))
for i in range(1, len(enter), 2):
    enter[i - 1], enter[i] = enter[i], enter[i - 1]
print(enter)