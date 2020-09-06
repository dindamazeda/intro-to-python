cat = {'color': 'black', 'type': 'house', 'age': 3}

print(cat['color'])

cat['color'] = 'white'
print(cat)


for key in cat:
    print(key)

for key, value in cat.items():
    print(key, value)