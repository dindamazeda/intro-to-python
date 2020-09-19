# Napisati program koji od korisnika uzima dve reči
# Zatim isprintati obe reči kao jedan string gde su prva slova od obe reči zamenila mesta
### primer ###
# program: Upiši prvu reč
# korisnik: kontrola
# program: Upiši drugu reč
# korisnik: taktika
# program: tontrola kaktika

first_word = input('Enter the first word: ')
second_word = input('Enter the second word: ')
print('{}{} {}{}'.format(second_word[0],first_word[1:],first_word[0],second_word[1:]))
