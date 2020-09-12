# Ask a user to enter a number
# Create a dictionary where the keys will start from 1 up until that number and the values is a square from the key
### example ###
# program: Enter a number
# user: 5
# program: 1: 1, 2: 4, 3: 9, 4: 16, 5: 25

input_key = int(input('Enter a number: '))

list_key = []
for x in range(1, input_key + 1):
    list_key.append(x)

# print(list_key)
# question: how to create list from loop "in range" in one line?
# answer: list_key = [x for x in range(1, input_key + 1)]

list_squared = [x ** 2 for x in list_key]

# print(list_squared)
dictionary_number = {}

for x in range(input_key):
    dictionary_number[list_key[x]] = list_squared[x]

print(dictionary_number)

# alternative
for x in range(1, input_key + 1):
    dictionary_number[x] = x ** 2

print(dictionary_number)

new_dictionary = {x: x ** 2 for x in range(1, input_key + 1)}

print(new_dictionary)
