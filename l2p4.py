enter = input('Запешите предложение... ').split()
for word, limiter in enumerate(enter, 1):
    print(f"{word}, {limiter[:10]}")