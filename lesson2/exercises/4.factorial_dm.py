# Write a number that will calculate a factorial for that number
# Write two version of this program, one with a for loop and another with while loop
# The factorial of number 5 (the notation is 5!) is 1 * 2 * 3 * 4 * 5 = 120
### example ###
# program: Enter a number and I will calculate a factorial for you
# user: 6
# program: 6! is 720

number_str = input('Enter a number and I will calculate a factorial for you: ')
number = int(number_str)

factorial = 1

# for x in range(1, number + 1):
#     factorial = x * factorial
# print('{}! is {}'.format(number, factorial))

x = 1
while x <= number:
    factorial *= x
    x +=1
print('{}! is {}'.format(number, factorial))