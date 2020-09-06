# Ask a user to enter some word
# Turn that word into a list of letters
# Print out the letters in reverse order by using list slicing
### example ###
# program: Enter a word
# user: pandora
# program: Your word in reverse order is arodnap

input_word = input('Enter a word:\n')
print('Your word in reverse order is {}'.format(input_word[::-1]))

list_word = []
for n in reversed(input_word):
    # print(n)
    list_word.append(n)
print('Your word in reverse order is {}'.format(list_word))

print(list(reversed(input_word)))


l = [w for w in reversed(input_word)]

print(l)

print('Your word in reverse order is {}'.format(input_word[::2]))

