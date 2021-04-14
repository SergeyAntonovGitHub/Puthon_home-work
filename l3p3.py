def my_func(arg_1, arg_2, arg_3):
    print('=' * 100)
    list = [arg_1, arg_2, arg_3]
    try:
        list.remove(min(list))
        print(f'Результат после искючения минимального значения списка: {list}')
        print('=' * 100)
        return sum(list)
    except TypeError:
        return 'Ошибка типа '

print(my_func(int(input('1 число - ')), int(input('2 число - ')), int(input('3 число - '))))