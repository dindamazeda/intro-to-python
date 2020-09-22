# DRUGI ZADATAK
# Dat je tekst ispod. Napisati program koji će da prebroji koliko se puta svaka reč pojavljuje u datom tekstu.
# Program mora da ignoriše mala ili velika slova npr. ako je dat tekst -> 'Republika je republika' program treba da
# isprinta republika: 2, je: 1

tekst = 'Pop kopa bob ko pokopa pop bob. Miš uz pušku miš niz pušku. Na vrh brda vrba brda! Crn jarac, crn trn, crn brsti trn na vrh brda pop jede bob!'
tekst = tekst.replace('.','')
tekst = tekst.replace('!','')
list_text = tekst.split(' ')
dictionary_word ={}

# print(list_text)

for x in list_text:
    x = x.lower()
    dictionary_word.setdefault(x,0)
    if x in dictionary_word:
        dictionary_word[x] +=1
print(dictionary_word)