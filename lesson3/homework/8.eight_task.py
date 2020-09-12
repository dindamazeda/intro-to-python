# OSMI ZADATAK
# # Uz pomoć while petlje napisati program koji će da isprinta sledeću šemu
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# Eight Task
# Using a while loop, write a program that will print the following scheme
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# star = '*'
# x = 1
# while x <= 5:
#     print('{}'.format(star * x))
#     x += 1
#
# y = 1
# while y <= 5:
#     print('{}'.format(star * (5 - y)))
#     y += 1


times_to_loop = 9
index = 1

number_of_stars = 1

while index <= 9:

    print('{}'.format('*' * number_of_stars))

    if index >= 5:
        number_of_stars -= 1
    else:
        number_of_stars += 1

    index += 1


