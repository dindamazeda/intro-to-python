# Dat je spisak pozicija u preduzeću i njihovih primanja. Napraviti nov rečnik u kom će se
# naći samo pozicije koje zarađuju više od 50000 din

platni_razredi = {'poslovođa': 65000, 'čistačica': 35000, 'menadžer': 85000, 'direktor': 120000,
                  'sekretarica': 45000, 'vozač': 40000, 'stažista': 20000}

remove = []
new_salaries = {}

for x in platni_razredi.keys():
    if platni_razredi[x] > 50000:
        new_salaries[x] = platni_razredi.get(x)
#        platni_razredi.pop(x)
# Error: dictionary changed size during iteration
