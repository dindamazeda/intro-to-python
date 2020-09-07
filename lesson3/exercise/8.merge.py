# write a program that create a list of 3 favourite meals and 3 favourite drinks from the user
# Merge the two lists into a third one and print it

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