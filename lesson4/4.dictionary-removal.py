pricing = {'banane': 127.5, 'kivi': 119.8, 'limun': 220.3, 'lubenica': 84.4, 'grejpfrut': 255.8, 'jabuke': 65.3, 'ananas': 182}

banana_price = pricing.pop('banane')
print(banana_price)
print(pricing)


last_element_that_was_insterted = pricing.popitem()
print(last_element_that_was_insterted)
print(pricing)


pricing.clear()
print(pricing)