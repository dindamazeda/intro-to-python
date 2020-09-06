macka = {'boja': 'crna', 'tip': 'kucna', 'godine': 3}

print(macka['boja'])

macka['boja'] = 'bela'
print(macka)


for key in macka:
    print(key)

for key, value in macka.items():
    print(key, value)