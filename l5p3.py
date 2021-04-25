with open('p3.txt', 'r', encoding='utf-8') as file:
    average_salary = []
    poor_employees = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            poor_employees.append(i[0])
        average_salary.append(i[1])
print(f'сотрудники с ЗП менее 20000 {poor_employees}')
print(f'средняя ЗП {sum(map(int, average_salary)) // len(average_salary)}')