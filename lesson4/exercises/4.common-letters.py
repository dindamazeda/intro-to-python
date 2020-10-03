# Napisati program koji će od korisnika da uzme tri reči
# Zatim pronaći sva zajednička slova između te tri reči
### primer ###
# Upiši prvu reč: makedonija
# Upiši drugu reč: dramaturgija
# Upiši treću reč: aerodrom
# program: Pronašao sam 3 slova koja se pojavljuju u svakoj reči a to su slova m, d, a

first_word = input('Enter the first word: ')
second_word = input('Enter the second word: ')
third_word = input('Enter the third word: ')


# rewrite this using set
list_letter = []
for x in first_word:
    if x in second_word and x in third_word:
        list_letter.append(x)


# do not do this - changing list/dictionary that you are iterating over
for x in list_letter:
   if x not in list_letter:
       list_letter.remove(x)

print ('I found {} letters that appears in each words, they are {}'.format(len(list_letter),list_letter))

# Q: how to write the program in one loop??
