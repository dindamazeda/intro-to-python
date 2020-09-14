fruits = ['banane', 'kivi', 'limun', 'lubenica', 'grejpfrut', 'jabuke', 'ananas']
prices = [127.5, 119.8, 220.3, 84.4, 255.8, 65.3, 182]

# old way
pricing_1 = {}

for index in range(len(fruits)):
    pricing_1[fruits[index]] = prices[index]

# new way
pricing_2 = {fruit: price for fruit, price in zip(fruits, prices)}

print(pricing_1)
print(pricing_2)
print(pricing_1 == pricing_2)