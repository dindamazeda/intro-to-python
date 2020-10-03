# Napisati program koji pita korisnika da upiše neku reč a zatim ispiše koliko se svako slovo ponavalja puta u toj reči
# Koristiti setdefault i get funkcije
### primer ###
# program: Napiši neku reč i ja ću ti reći koliko se puta svako slovo ponavlja
# korisnik: google
# program: g: 2, o: 2, l: 1, e: 1

input_word = input('Write a word and I will tell you how many times each letter is repeated \n')

dictionary_word = {}

for x in input_word:
    dictionary_word.setdefault(x, 0)
    if x in dictionary_word:
        dictionary_word[x] += 1
print(dictionary_word)
