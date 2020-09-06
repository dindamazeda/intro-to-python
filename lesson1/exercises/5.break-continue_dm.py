# write a for loop that will all numbers from 0 to 6 except 3 i 6
# use continue
### example ###
# expected output -> 0 1 2 4 5

for number in range(0, 7):
    if number == 3 or number == 6:
        continue
    print(number)

# write a loop that will take some word from the user (use input() function) i print out all consonants in that word
### example ###
# program: Enter some word
# user: singapore
# program: All consonats in this word are sngpr

user_input = input('Enter some word: ')
vowel = ['a', 'i', 'u', 'e', 'o']
print('All consonant in this word are :')
for letters in user_input:
    if letters in vowel:
        continue
    print(letters)
