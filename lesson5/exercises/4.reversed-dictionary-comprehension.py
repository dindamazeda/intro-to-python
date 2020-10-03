# Dat je rečnik. Napisati program koji će uz pomoć dictionary comprehension da zameni mesta za ključeve i vrednosti u novom rečniku
# recnik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Očekivani rezultat -> {1: 'a', 2: 'b' itd. }

recnik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# new_dictionary = {}
# for x in recnik.keys():
#     new_dictionary[recnik[x]]= x

new_dictionary = {new_key : new_value for (new_value,new_key) in recnik.items()}

print(new_dictionary)