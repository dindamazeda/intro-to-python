# Napisati program koji od korisnika uzima neku reč i zatim od prva 2 i poslednja 2 slova te reči napraviti novu reč
### primer ###
# program: Upiši neku reč
# korisnik: kornet
# program: Tvoja reč je -> koet

input_word = input('type a word: ')
list_input_word = list(input_word)
output_word = [list_input_word[0],list_input_word[1],list_input_word[-2],list_input_word[-1]]
print('your word is {}'.format(''.join(output_word)))