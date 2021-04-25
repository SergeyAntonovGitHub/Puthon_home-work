rus_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('p4rus.txt', 'w', encoding='utf-8') as nf:
    with open('p4.txt', 'r', encoding='utf-8') as mf:
        nf.write(str([line.replace(line.split()[0], rus_words.get(line.split()[0])) for line in mf]))