# PETI ZADATAK
# Napisaćemo program koji utvrđuje frekventnost slova u srpskom jeziku nad datim tekstom
# Potrebno je ispisati rečnik sa slovom i procenat (udeo) tog slova u odnosu na ukupan broj slova
# npr. ako je dat tekst -> patka je slatka, program treba da zna sledeće:
# u tekstu ima 13 slova (razmaci se ne računaju kao slovo!) dok se slovo 'a' ponavlja 4 puta
# To znači da u rečniku treba da stoji a: 30.76 jer je toliki udeo (procenat) slova a u odnosu na ukupan broj slova
# Pažnja! - promenljiva koja je data ispod je i dalje string i ponaša se isto kao i svaki string bez obzira što je na više linija to je i dalje jedan string!
# U Pythonu su dozvoljeni stringovi na više linija (ako je tekst dugačak kao ovaj naš sada npr.) samo se umesto apostrofa ili navodnika stave 3 apostrofa ili 3 navodnika

# FIFTH TASK
# We will write a program that determines the frequency of letters in the Serbian language over a given text
# It is necessary to print a dictionary with the letter and the percentage (share) of that letter in relation to the total number of letters
#e.g. if the given text -> patka je slatka, the program should know the following:
# there are 13 letters in the text (spaces do not count as a letter!) while the letter 'a' is repeated 4 times
# This means that the dictionary should say a: 30.76 because that is the proportion of letters and in relation to the total number of letters
# Attention! - the variable given below is still a string and behaves the same as any string no matter that it is on multiple lines it is still a single string!
# In Python, multi-line strings are allowed (if the text is as long as ours now, for example) only 3 apostrophes or 3 quotation marks are placed instead of apostrophes or quotation marks


tekst = """Prestižno priznanje Man Buker u fokus najpre stavlja uži izbor koji je u septembru prošle godine imao šest knjiga.
Nagradu je, među autorima koji su pažnju posvetili osobenom istraživanju engleskog jezika, temama istraživanja bola, društvene i rodne nepravde,
kao i ugrožene prirode, prvi put osvojila autorka iz Severne Irske Ana Berns za roman Mlekadžija.
Ona je osvetlila problem zlostavljanja jedne mlade devojke.
Zašto se bavimo brojevima kada je u stvaralaštvu, u bilo kojoj umetničkoj oblasti, kvalitet najvažniji?
Upravo zbog toga što je i književno stvaranje oblast slobode u kojoj ne bi trebalo da vlada industrijalizacija kreacije, odnosno osrednjost u štancovanju."""


#tekst = 'Dinda , . Mazeda'
text = tekst.replace(' ','')
text = text.replace(',','')
text = text.replace('.','')
text = text.replace('?','')
text = text.replace('\n','')
list_text = list(text.lower())

dictionary_letter = {}

for x in list_text:
    dictionary_letter.setdefault(x,0)
    if x in dictionary_letter:
        dictionary_letter[x] +=1
    dictionary_letter [x] = round(dictionary_letter [x]/len(list_text)*100,3)
print (dictionary_letter)