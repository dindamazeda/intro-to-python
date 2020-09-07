# Napisati program koji će korisnika pitati da ukuca ime, prezime i datum rođenja
# Write a program that will ask te user to enter his name, lastname i date of birth
# Store all values in a dictionary
### example ###
# program: What is your name?
# korisnik: Marko
# program: What is your last name?
# korisnik: Markovic
# program: When were you born?
# korisnik: 25.5.1985.
# program: Thank you Marko. Your data is stored.

name = input('What is your name? ')
last_name = input ('What is your last name? ')
date = input ('When were you born? ')

dictionary_data = {'Name':name, 'Last Name':last_name, 'Date of Birth':date}
print ('Thank you {}. Your data is stored'.format(dictionary_data['Name']))
