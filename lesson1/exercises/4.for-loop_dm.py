# Write a for loop that will take some number from the user and print out all numbers from 0 up until that number (that number included)
# program: Enter one number
# user: 7
# program: 0, 1, 2, 3, 4, 5, 6, 7

user_input = input('Enter one number: ')
input_number = int(user_input)
for number in range(0, input_number + 1):
    print(number)
