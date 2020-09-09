# DEVETI ZADATAK
# # Uzeti broj od 1 do 10 do korisnika
# # Napisati program koji će da kaže koje su reči u datoj listi duže od onog broja koji je korisnik uneo
# # npr. ako je korisnik uneo broj 4, onda prikazati reči koje imaju više od 4 slova
# # auti = ['bmw', 'porsche', 'audi', 'yugo', 'mitsubishi', 'nisan', 'toyota', 'kia', 'volvo', 'chevrolet', 'mazda']
#
# Ninth Task
# Ask user to pick a number from 1 to 10
# Write a program that will say which words in a given list are longer than the number the user entered
# e.g if the user has entered the number 4, then display words that have more than 4 letters
# car = ['bmw', 'porsche', 'audi', 'yugo', 'mitsubishi', 'nisan', 'toyota', 'kia', 'volvo', 'chevrolet', 'mazda']

car = ['bmw', 'porsche', 'audi', 'yugo', 'mitsubishi', 'nisan', 'toyota', 'kia', 'volvo', 'chevrolet', 'mazda']
input_number=int(input('Pick a number from 1 to 10: '))

output_car = []
for x in car:
    if len(x) > input_number:
        output_car.append(x)
print(output_car)