# PETI ZADATAK
# Koristeći funkcije potrebno je da napravimo program koji obračunava plate a naš program će koristi zaposleni iz finansijskog odeljenja
# Program treba da uzme 2 vrednosti od korisnika, prva je broj sati koje je radnik odradio za ovaj mesec, a druga je cena po satu za tog radnika
# Kada program izračuna platu za taj mesec i ako ta plata spada u neku kategoriju visokih primanja, potrebno je na osnovu kategorizacije skinuti još dodatni procenat od te sume na ime poreza državi :)
# Kategorija za visoke plate se nalazi u rečniku ispod
### primer ###
# program: Upiši broj sati koje je radnik odradio za ovaj mesec
# korisnik: 154
# program: Upiši cenu za sat
# korisnik: 600
# program: Obračun za ovog korisnika iznosi 92400 dinara
# program: Korisnik spada u kategoriju visokih primanja 58000-93000 i mora da plati porez od 18%
# program: Suma koju treba isplatiti radniku je 75768 dinara


def function_tax(input_hour,input_price):
    salary = input_price * input_hour
    dictionary_taxes = {'35000-45000': 10, '45000-58000': 14, '58000-93000': 18, '93000-5000000': 25}
    tax = ''
    category = ''
    for x in dictionary_taxes.keys():
        y = x.split('-')
        if salary > int(y[0]) and salary < int(y[1]):
            tax = int(dictionary_taxes[x])
            category = x
    net_salary = salary - (salary * tax / 100)
    return (salary,tax,category,net_salary)

input_hour = int(input('Enter the number of hours the worker worked for this month: '))
# input_hour = 154
input_price = int(input('Enter the price per hour: '))
# input_price = 600

(salary,tax,category,net_salary) = function_tax(input_hour,input_price)

print('The bill for this user is {} dinars'.format((salary)))
print('The user belongs to the category of income {} and must pay a tax of {}'.format(category,tax))
print('The amount to be paid to the worker is {} dinars'.format(net_salary))
