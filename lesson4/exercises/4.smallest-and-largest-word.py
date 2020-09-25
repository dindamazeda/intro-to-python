# Napisati program koji će korisnika da pita za nekih 5 reči a zatim utvrditi koja je najkraća i najduža reč
# i ispisati koliki broj slova su imale te reči

input_word = []
for x in range(1, 6):
    input_word.append(input('Enter a word ({}/5) : '.format(x)))

print('The shortest word is {} and it has {} letters'.format(min(input_word), len(min(input_word))))
print('The longest word is {} and it has {} letters'.format(max(input_word), len(max(input_word))))
