#TREĆI ZADATAK
# Napisati program koji će pronaći slične reči u datom tekstu ispod
# Kako definišemo sličnost? Ako uzmemo neke dve reči npr. kratak i patka ove dve reči imaju tri zajednička slova (a,t i k) i njihova sličnost će biti 3
# Što je veći broj zajedničkih slova to je sličnost veća
# Program treba da uporedi svaku reč i da napravi parove reči i da ispiše njihovu sličnost npr. ako imamo tekst
# Patka je kratka -> treba da dobijemo patka-kratka: 3, patka-je: 0, je-kratka: 0
# Obratite pažnju da u finalnom ispisu eliminišete "duple parove" npr. patka-kratka: 3 i kratka-patka: 3 ćemo smatrati duplikatima tako da je dovoljno ostaviti samo jedan unos

#tekst = 'hajka je bajka koja vreba iz prikrajka dok je Barevo naselje gde ne manjka veselje'
tekst = 'dinda mazeda dina'
set_key = set(tekst.split(' '))
key = list(set_key)

dictionary_tekst = {}
index = len(key)

# create keys of word pairs and eliminate the duplicated pairs
for y in range(index):
    for x in range(1,index):
        if y != x:
            if x > y:
                dictionary_tekst.setdefault(('{}-{}'.format(key[y],key[x])),[])

# find the similiarity between each key
for x in dictionary_tekst:
    list_letter = []
    letter = x.split('-')
    for y in letter [0]:
        if y in letter[1]:
            list_letter.append(y)
#            dictionary_tekst[x]=list_letter
            dictionary_tekst[x]=set(list_letter)

print(dictionary_tekst)


