# +-------+-----------+-----+---------------+
# | Ime   | Zanimanje | Pol | Mesto rođenja |
# +-------+-----------+-----+---------------+
# | Pera  | Postar    | M   | Beograd       |
# +-------+-----------+-----+---------------+
# | Vesna | Doktor    | Z   | Valjevo       |
# +-------+-----------+-----+---------------+
# | Marko | Programer | M   | Kraljevo      |
# +-------+-----------+-----+---------------+


pera = {'zanimanje': 'Postar', 'pol': 'M', 'mesto': 'Beograd'}
vesna = {'zanimanje': 'Doktor', 'pol': 'Ž', 'mesto': 'Valjevo'}
marko = {'zanimanje': 'Programer', 'pol': 'M', 'mesto': 'Kraljevo'}


recnik_osoba = {'pera': pera, 'vesna': vesna, 'marko': marko}

print(recnik_osoba['marko']['zanimanje'])