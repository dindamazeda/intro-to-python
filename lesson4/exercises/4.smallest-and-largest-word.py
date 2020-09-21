# Napisati program koji će korisnika da pita za nekih 5 reči a zatim utvrditi koja je najkraća i najduža reč
# i ispisati koliki broj slova su imale te reči

input_word = []
dictionary_word = {}
for x in range (1,6):
    input_word.append(input('Enter a word ({}/5) : '.format(x)))

for x in input_word:
    dictionary_word [x] = len(x)

short_word = min(dictionary_word.values())
long_word = max(dictionary_word.values())

for x in dictionary_word:
    if dictionary_word[x] == short_word:
        print('The shortest word is {} and it has {} letters'.format(x,len(x)))
    elif dictionary_word [x] == long_word:
        print('The longest word is {} and it has {} letters'.format(x,len(x)))