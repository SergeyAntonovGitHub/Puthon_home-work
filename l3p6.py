def int_func(words):
    alphabet = 'qazwsxedcrfvtgbyhnujmikolp'
    return words.title() if not set(words).difference(alphabet) else False

enter = input('Введите строкук из слов, разделенных пробелом. Слово должны состоять из латинских маленьких букв ').split()
for text in enter:
    resultat = int_func(text)
    print(resultat)