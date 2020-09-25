# Napisati program koji od korisnika uzima neku reč i zatim od prva 2 i poslednja 2 slova te reči napraviti novu reč
### primer ###
# program: Upiši neku reč
# korisnik: kornet
# program: Tvoja reč je -> koet

input_word = input('type a word: ')
output_word = [input_word[0], input_word[1], input_word[-2], input_word[-1]]
print('your word is {}'.format(''.join(output_word)))
