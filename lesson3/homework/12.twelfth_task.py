# DVANAESTI ZADATAK
# # Data su dva rečnika. Napisati program koji će da spoji dva rečnika u treći
# # prvi_recnik = {'a': 10, 'b': 20, 'c': 30}
# # drugi_recnik = {'d': 40, 'e': 50, 'f': 60}
#
# Twelfth Task
# Two dictionaries are given. Write a program that will merge two dictionaries into a third
# first_dictionary = {'a': 10, 'b': 20, 'c': 30}
# second_dictionary = {'d': 40, 'e': 50, 'f': 60}


first_dictionary = {'a': 10, 'b': 20, 'c': 30}
second_dictionary = {'d': 40, 'e': 50, 'f': 60}

merged_dictionary = {**first_dictionary,**second_dictionary}
print(merged_dictionary)