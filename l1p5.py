firm_proceeds = int(input("Введите сумму выручки фирмы(р): "))
firm_costs = int(input("Введте сумму издержек фирмы(р): "))
if firm_proceeds > firm_costs:
    print("Фирма отработала в прибыль")
else:
    print("Фирма отработала в убыток")
profit = firm_proceeds - firm_costs
print("Прибыль стоставляет(р): ", profit)
print("Рентабельность(%) - " "{:.0f}".format (profit / firm_proceeds * 100))

number_of_workers = int(input("Введите колличество сотрудников: "))
print("Приыбль фирмы на одного сотрудника состовляет(р): " "{:.0f}".format (profit / number_of_workers))