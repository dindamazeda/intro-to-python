# ČETVRTI ZADATAK
# # Napisati program koji će uzeti neku reč od korisnika.
# # Nakon toga zameniti svaki samoglasnik sa znakom uzvika -> !
# ### primer ###
# # program: Napiši neku reč:
# # korisnik: tranzicija
# # program: tr!nz!c!j!
#
# Fourth Task
# Write a program that will take a word from the user.
# Then replace each vowel with an exclamation mark ->!
# Example
# program: Write a word:
# user: tranzicija
# program: tr!nz!c!j!

input_word = input('Write a word: ')
output_word = []

vowel = ['a','i','u','e','o']
# for x in input_word:
#     if x in vowel:
#         output_word.append('!')
#     else:
#         output_word.append(x)
#
# print(output_word)

for x in vowel:
    if x in input_word:
        input_word = input_word.replace(x, '!')
print(input_word)