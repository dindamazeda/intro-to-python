# +-------+-----------+-----+---------------+
# | name   | profession | sex | Place of birth |
# +-------+-----------+-----+---------------+
# | Pera  | Postar    | M   | Beograd       |
# +-------+-----------+-----+---------------+
# | Vesna | Doktor    | Z   | Valjevo       |
# +-------+-----------+-----+---------------+
# | Marko | Programer | M   | Kraljevo      |
# +-------+-----------+-----+---------------+


pera = {'profession': 'Postar', 'sex': 'M', 'place-of-birth': 'Beograd'}
vesna = {'profession': 'Doktor', 'sex': 'Ž', 'place-of-birth': 'Valjevo'}
marko = {'profession': 'Programer', 'sex': 'M', 'place-of-birth': 'Kraljevo'}

#dictionary_person
recnik_osoba = {'pera': pera, 'vesna': vesna, 'marko': marko}

print(recnik_osoba['marko']['profession'])