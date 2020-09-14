list_of_letters = ['p', 'e', 'r', 'a']
pera = ''.join(list_of_letters)
print(pera)

animals = ['krava', 'pas', 'macka', 'vuk']

print('|'.join(animals))
print(','.join(animals))
print(' '.join(animals))
print('.'.join(animals))
print('!'.join(animals))


joint_string = '1,2,3,4,5,6'
some_other_joint_string = '34;Pera;Beograd;pekar'

print(joint_string.split(','))
print(some_other_joint_string.split(';'))