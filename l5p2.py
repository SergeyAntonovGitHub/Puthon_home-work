with open('p2.txt', 'r', encoding='utf-8') as f:
    gen_spisok = [f'{number}. {" ".join(stroka.split())} - {len(stroka.split())} слов '
                  for number, stroka in enumerate(f, 1)]
    print(*gen_spisok, f'всего строк - {len(gen_spisok)}.', sep='\n')