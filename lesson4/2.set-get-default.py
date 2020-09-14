pricing = {'banane': 127.5, 'kivi': 119.8, 'limun': 220.3, 'lubenica': 84.4, 'grejpfrut': 255.8, 'jabuke': 65.3, 'ananas': 182}


# KeyError
# print(cenovnik['mango'])

print(pricing.get('mango'))


available_quantity = {}
products = ['brasno', 'mleko', 'hleb']

for product in products:
    available_quantity.setdefault(product, 0)

print(available_quantity)

print(available_quantity.setdefault('brasno', 22))
print(available_quantity)