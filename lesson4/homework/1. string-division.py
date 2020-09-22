# PRVI ZADATAK
# Treba da podelimo neki string na 2 dela
# Ako taj string ima paran broj slova onda ćemo dobiti dva jednaka dela
# Ako string ima neparan broj slova onda će ono slovo viška završiti u prvom delu stringa
# Npr. ako je dat string 'abcde', nakon podele dobićemo dva stringa i to prvi string će biti 'abc' a drugi string 'de'
# Napisati program koji će da uzme dve reči, podeli ih i izvrši sledeću operacije nad njima
# prva-rec-prvi-deo + druga-rec-prvi-deo + prva-rec-drugi-deo + druga-rec-drugi-deo
### primer ###
# program: Upiši dve reči
# korisnik: macka parmezan
# program: macparmkaezan


# FIRST TASK
# We need to divide a string into 2 parts
# If that string has an even number of letters then we will get two equal parts
# If the string has an odd number of letters then that redundant letter will end up in the first part of the string
# For example. if the string 'abcde' is given, after division we will get two strings and the first string will be 'abc' and the second string 'de'
# Write a program that will take two words, divide them and perform the next operation on them
# first-word-first-part + second-word-first-part + first-word-second-part + second-word-second-part
### example ###
# program: Type two words
# user: macka parmezan
# program: macparmkaezan

input_word = input('Type 2 words: ')

list_word = input_word.split(' ')
word_one = list_word[0]
word_two = list_word[1]
index_one = divmod(len(list_word[0]), 2)
index_two = divmod(len(list_word[1]), 2)

output_word = [word_one[:index_one[0] + index_one[1]], word_two[:index_two[0] + index_two[1]],
               word_one[index_one[0]:],word_two[index_two[0]:]]

print(''.join(output_word))



