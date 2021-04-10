spisok = [9, 8, 7, 6, 5, 4, 3, 2, 1]
enter = int(input("Введите элимент рейтинга: "))
i = 0
for number in spisok:
    if enter <= number:
        i += 1
spisok.insert(i, int(enter))
print(spisok)