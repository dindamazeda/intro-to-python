# Write a program that will ask the user for a word and the count how many times each letter appears in that word
### example ###
# program: Enter a word
# user: google
# program: g: 2, o: 2, l: 1, e: 1

word = input('Enter a word: ')
frequency = {}

for x in word:
    # print(x)
    if x in frequency:
        frequency[x] += 1

    frequency.setdefault(x, 1)

    # else:
    #   frequency[x] = 1

print(frequency)
