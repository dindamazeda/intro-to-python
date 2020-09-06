# Create list of numbers from 0 to 10 but with a random order (import random - see random module and usage)
# Go through the list and on every iteration as a user to guess a number between 0 and 10
# At end the program needs to print how many times the user had correct and incorrect guesses
# random_numbers = [5, 1, 3, 9, 7, 2, 4, 6, 8]
# program: Guess a number between 0 and 10.
# (If we look at the above list the current number is 5) user: 8
# program: That is not a correct number. Try to guess a new number between 0 and 10.
# (If we look at the above list the next number is 1) user: 1
# program: Bravo! That is the correct number. Try to guess a new one.
# The program continues until the end of the list...
# program: Congratulations. You've guessed the correct number 3 times and 7 times you were not correct.

import random

numbers = []
correct = 0
wrong = 0

for x in range(0, 9):
    numbers.append(random.randint(0,10))
print(numbers)

# for y in numbers:
#     input_number = int(input('Guess a number between 0 and 10: '))
#     if input_number == y:
#         print('Bravo! That is the correct number. Try to guess a new one')
#         correct +=1
#     else:
#         print('That is not a correct number. Try to guess a new number between 0 and 10')
#         wrong +=1
#
# print ('You have guessed the correct number {} times and {} times you were not correct'.format(correct, wrong))

x = len(numbers)
index = 0
while index < x:
    input_number = int(input('Guess a number between 0 and 10: '))

    if index == len(numbers):
        break

    if input_number == numbers[index]:
        print('Bravo! That is the correct number. Try to guess a new one')
        correct += 1
    else:
        print('That is not a correct number. Try to guess a new number between 0 and 10')
        wrong += 1

    index += 1