# TRINAESTI ZADATAK
# # Dat je rečnik sa proizvodima i njihovim cenama
# # Napisati program koji će da od korisnika uzme neku cifru i da kaže koji proizvodi su skuplji od te cifre
# ### primer ###
# # proizvodi = {'banane': 129, 'kivi': 188, 'limun': 232, 'lubenica': 98, 'grejpfrut': 203, 'jabuke': 75, 'ananas': 176}
# # program: Unesi neku cenu
# # korisnik: 150
# # program: Proizvodi koji su skuplji od 150din su kivi, limun, grejpfrut, ananas
#
# Thirteen Task
# A dictionary with products and their prices is given
# Write a program that will take a number from the user and say which products are more expensive than that number
# Example
# products = {'bananas': 129, 'kiwi': 188, 'lemon': 232, 'watermelon': 98, 'grapefruit': 203, 'apples': 75, 'pineapple': 176}
# program: Enter a price
# users: 150
# program: Products that are more expensive than 150 dinars are kiwi, lemon, grapefruit, pineapple
output = []
products = {'bananas': 129, 'kiwi': 188, 'lemon': 232, 'watermelon': 98, 'grapefruit': 203, 'apples': 75, 'pineapple': 176}
input_price = int(input('Enter a price: '))
for x in products:
    price = products.get(x)
    if price > input_price:
        output.append(x)
print('Products that are more expensive than {} dinars are {}'.format(input_price, output))