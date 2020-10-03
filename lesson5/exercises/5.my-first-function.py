# Napisati funkciju koja će da kvadrira broj koji je uzet od korisnika

def squared(input_number):
    input_number = float(input_number)
    return input_number*input_number

input_number = input('please enter a number: ')
print('Square result of your number is {}'.format(squared(input_number)))
