def num(x, y):
    try:
        x, y = int(x), int(y)
        z = x / y
    except ValueError:
        return 'error'
    except ZeroDivisionError:
        return 'not'
    return round(z)

print(num(input('1 - '), input('2 - ')))