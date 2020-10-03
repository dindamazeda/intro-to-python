# Napisati funkciju koja će da pronađe i ispiše sve neparne brojeve u zadatom opsegu. Opseg uzeti od korisnika
### primer ###
# program: Upiši neki opseg
# korisnik: 1, 13
# program: 1, 3, 5, 7, 9, 11, 13

def odd_number_range(input_range):
    input_range = (input_range.split(','))
    odd_number = []
    for x in range (int(input_range[0]),int(input_range[1])):
        if x % 2 != 0:
            odd_number.append(x)
    return odd_number

input_range = input('please enter a range: ')

print(odd_number_range(input_range))