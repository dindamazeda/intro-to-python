# Data su dva rečnika.
# Od ova dva rečnika napraviti listu gde će elementi biti ključevi prvog rečnika i vrednosti drugog rečnika

prvi_recnik = {'tramvaj': 7, 'autobus': 25, 'trolejbus': 28, 'e-bus': 'eko1', 'metro': None}
drugi_recnik = {7: 'Ustanicka', 25: 'Kumodraž', 28: 'Zvezdara', 1: 'Vukov spomenik'}

output_list = []
for key in prvi_recnik.keys():
    output_list.append(key)

for value in drugi_recnik.values():
    output_list.append(value)

print(output_list)