# DRUGI ZADATAK
# Dat je niz brojeva. Napisati program koji će ispise najmanji i najveći broj iz niza
# niz_brojeva = [15, 116, 54, 30, 21, 41, 65, 7, 105, 135, 173, 56, 197, 56, 136, 83, 97, 130, 184, 112, 83, 157, 189, 24, 28, 127, 166, 99, 37, 114, 3, 123, 160, 97, 152]
#
# Second Task
# a list of numbers is given. Write a program that print the smallest and largest number from the list
# list_of_numbers = [15, 116, 54, 30, 21, 41, 65, 7, 105, 135, 173, 56, 197, 56, 136, 83, 97, 130, 184, 112, 83, 157, 189, 24, 28, 127, 166, 99, 37, 114, 3, 123, 160, 97, 152]

list_of_number = [15, 116, 54, 30, 21, 41, 65, 7, 105, 135, 173, 56, 197, 56, 136, 83, 97, 130, 184, 112, 83, 157, 189, 24, 28, 127, 166, 99, 37, 114, 3, 123, 160, 97, 152]
sorted_list = sorted(list_of_number)
print('The smallest number is {} and the largest number is {}'. format(sorted_list[0],sorted_list[-1]))
