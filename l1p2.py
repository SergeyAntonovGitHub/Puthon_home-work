number = int(input("Введите время в (c) "))
hour = number // 3600
minute = (number - hour * 3600) // 60
second = number - (hour * 3600 + minute * 60)
print(f"Время в формате чч:мм:сс   {hour:02} : {minute:02} : {second:02}")
