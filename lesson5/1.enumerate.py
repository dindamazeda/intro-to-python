reverse_order = reversed(['a', 'b', 'c', 'd', 'e'])
ordered_numbers = sorted([83, 3, 92, 22, 31, 83, 14, 54, 72])

for index, letter in enumerate(reverse_order):
    print('Letter {} has an index of {}'.format(letter, index))

for index, number in enumerate(ordered_numbers):
    print('Number {} has an index of {}'.format(number, index))
