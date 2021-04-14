def info(**kwargs):
    return '|'.join(kwargs.values())

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthday = input('Введите год вашего рождения: ')
city = input('Введите город, где вы проживаете: ')
email = input('Введите ваш email: ')
phone = input('Введите ваш номер телефона: ')


print(info(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))