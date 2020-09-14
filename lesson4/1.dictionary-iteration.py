dictionary = {'banane': 127.5, 'kivi': 119.8, 'limun': 220.3, 'lubenica': 84.4, 'grejpfrut': 255.8, 'jabuke': 65.3, 'ananas': 182}

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print('Key is {}, and value is {}'.format(key, value))