my_spisok = [50, 31, 40, 51, 60, 51, 78, 21, 53, 52]
my_gen = [my_spisok[i] for i in range(1, len(my_spisok)) if my_spisok[i] > my_spisok[i-1]]
print(my_gen)