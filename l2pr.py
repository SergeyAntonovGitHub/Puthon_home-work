enter = int(input("Введите целое число от 1 до 12: "))
season_l = ["winter", "spring", "summer", "autumn", "winter"]
season_d = {0: "winter", 1: "spring", 3: "summer", 4: "winter"}
print(f"1 - {season_l[enter // 3]}\n2 - {season_d[enter // 3]}")