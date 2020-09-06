# Christmas tree - write a program that will print out the christmas tree with a for loop
### example ###
# Program :
#
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

# star = ['*']
# print (star)
# for x in range (7):
#     for y in range (2):
#         star.append('*')
#     print (star)

star = '*'
space = ' '
for x in range(7):
    y = x * 2 - 1
    z = 7 - x
    print('{}{}'.format(space * z, star * y))

# Multiplication table - write a program that takes an input from user (some number) and writes a multiplication table (last multiplier can be 10)
### example ###
# program: Please enter one number
# user: 5
# program:
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50

user_input = input('Please enter one number: ')
# number = float(user_input)
number = int(user_input)
for x in range(1, 11):
    result = number * x
    print('{} * {} = {}'.format(number, x, result))


for number in reversed(range(10)):
    print(number)