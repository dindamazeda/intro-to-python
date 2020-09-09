# ŠESTI ZADATAK
# # Napisati program koji će da uzme dve liste i od njih napravi dictionary gde će elementi prve liste biti ključevi, a elementi druge liste vrednosti
# ### primer ###
# # voce = ['banane', 'kivi', 'limun', 'lubenica', 'grejpfrut', 'jabuke', 'ananas']
# # cene = [127.5, 119.8, 220.3, 84.4, 255.8, 65.3, 182]
# program: {'banane': 127.5, 'kivi': 119.8 itd. }
#
# Sixth Task
# Write a program that will take two lists and make a dictionary out of them where the elements of the first list will be the keys and the elements of the second list the values
# Example
# # fruit = ['bananas', 'kiwi', 'lemon', 'watermelon', 'grapefruit', 'apples', 'pineapple']
# # prices = [127.5, 119.8, 220.3, 84.4, 255.8, 65.3, 182]
# program: {'bananas': 127.5, 'kiwis': 119.8, etc.}

fruit = ['bananas', 'kiwi', 'lemon', 'watermelon', 'grapefruit', 'apples', 'pineapple']
prices = [127.5, 119.8, 220.3, 84.4, 255.8, 65.3, 182]
dictionary_fruit = {}
for x in range(len(fruit)):
    dictionary_fruit[fruit[x]] = prices[x]
print(dictionary_fruit)
