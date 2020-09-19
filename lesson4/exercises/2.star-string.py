# Napisati program koji od korisnika uzima neku reč
# Zatim svako ponavljanje prvog slova od te reči zameniti sa zvezdicom osim prvog slova
### primer ###
# program: Napiši neku reč
# korisnik: kokoska
# program: ko*os*a

input_word = input('Write a word: ')
star_word = input_word.replace(input_word[0], '*')
print('{}{}'.format(input_word[0],star_word[1:]))
