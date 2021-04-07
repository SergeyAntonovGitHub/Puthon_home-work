a = int(input("Введите результат 1-го дня(км): "))
b = int(input("Введите окончтаельный результат(км): "))
result = 1
km = a
while km < b:
    a = a + 0.1 * a
    result += 1
    km = a
print(f"Вы достигнете нужной цели на %.d день" % result)
