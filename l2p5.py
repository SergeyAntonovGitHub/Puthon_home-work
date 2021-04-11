spisok = [9, 8, 7, 6, 5, 4, 3, 2, 1]
enter = int(input("Введите элимент рейтинга: "))
count = 0
for number in spisok:
    if enter <= number:
        count += 1
spisok.insert(count, int(enter))
print(spisok)