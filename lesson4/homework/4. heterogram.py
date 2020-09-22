# ČETVRTI ZADATAK
# Napisati program koji će za svaku reč u datom tekstu reći da je li je ta reč heterogram ili nije
# Heterogram je reč u kojoj se svako slovo pojavljuje samo jednom npr. reč bajkovit je heterogram dok reč bajka nije heterogram jer se slovo a ponavlja 2 puta
# Ako je dat tekst -> bajkovit je bajka -> program treba da ispiše sledeće:
# program: bajkovit je heterogram
# program: je je heterogram
# program: bajka nije heterogram

tekst = 'centrifuga je sila kojom se upravljaju veš mašine'
list_text = tekst.split(' ')

for x in list_text:
   temp = set(x)
   if len (x) == len(temp):
       print('{} is heterogram'.format(x))
   else:
       print('{} is not heterogram'.format(x))