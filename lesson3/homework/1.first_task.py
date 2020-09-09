# PRVI ZADATAK
#
# Napisati program koji će da uzme 3 omiljena jela od korisnika i smesti ih u listu
# Zatim program treba da uzme 3 omiljena pića od korisnika i smesti ih u drugu listu
# Spojiti sve to u treću listu i isprintati treću listu
#
# First Task
# Write a program that will ask 3 favourite meals from user and put them on a list
# Then the program should ask 3 favourite drinks from user and put them on a list
# Merge it all into the third list and print the third list

input_meals = []
input_drinks = []
for x in range (3):
    input_meals.append(input('What are your favourite meals({}/3) ? '.format(x+1)))
    input_drinks.append(input('What are your favourite drinks({}/3) ? '.format(x + 1)))
# print(input_meals)
# print(input_drinks)

all_favourite = []
all_favourite.extend(input_meals)
all_favourite.extend(input_drinks)

print(all_favourite)