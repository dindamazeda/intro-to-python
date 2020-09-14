fish_meals = ['šaran', 'smuđ', 'pastrmka', 'som', 'oslić']
drinks = ['crveno vino', 'belo vino', 'pivo', 'rakija', 'viski']

for fish, drink in zip(fish_meals, drinks):
    print('Fish {} goes well with {}'.format(fish, drink))




letters = ['a', 'b', 'c', 'd', 'e', 'f']
numbers = [4, 9, 10, 5, 8, 7, 2, 1]
roman_numbers = ['X', 'M', 'C', 'L', 'I']

for letter, number, roman_number in zip(letters, numbers, roman_numbers):
    print('letter {} and number {} and roman number {}'.format(letter, number, roman_number))