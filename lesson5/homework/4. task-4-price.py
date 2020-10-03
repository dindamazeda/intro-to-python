# ČETVRTI ZADATAK
# # Dat je rečnik sa proizvodima i njihovim cenama
# # Napisati program koji će da od korisnika uzme neku cifru i da ispiše listu proizvoda koji su skuplji od te cifre.
# # Program treba da bude napisan na 4 linije koda od kojih prvu liniju već imate ispod (promenljiva proizvodi) :)
# ### primer ###
# # proizvodi = {'banane': 129, 'kivi': 188, 'limun': 232, 'lubenica': 98, 'grejpfrut': 203, 'jabuke': 75, 'ananas': 176}
# # program: Unesi neku cenu
# # korisnik: 150
# # program: Proizvodi koji su skuplji od 150din su kivi, limun, grejpfrut, ananas

proizvodi = {'banane': 129, 'kivi': 188, 'limun': 232, 'lubenica': 98, 'grejpfrut': 203, 'jabuke': 75, 'ananas': 176}
input_price = int(input('enter a price: '))
output_product={product:price for (product,price) in proizvodi.items() if price > input_price}
print('Product that are more expensive than {} are {}'.format(input_price, [key for key in output_product]))