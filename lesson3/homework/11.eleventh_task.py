# JEDANAESTI ZADATAK
# # Pravićemo igru vešala, primer ovde -> http://www.losprimjer.com/vjesanje.php
# # Naravno naša će biti malo drugačija...
# # Reč koju korisnik treba da pogodi definišete sami kao neki string npr. rec_za_pogadjanje = 'smrdibuba'
# # Korisnik ima neograničen broj pokušaja
# # Kada svaki put korisnik unese slovo treba reći da li je pogodio neko slovo i treba isprintati delovi reči koje je pogodio do sada
# # Kada korisnik pogodi reč, treba isprintati koliko pokušaja mu je bilo potrebno da pogodi reč
# ### primer ###
# # program: Zamislio sam neku reč. Upiši neko slovo i na taj način pokušaj da pogodiš reč (pretpostavimo da je reč smrdibuba)
# # korisnik: b
# # program: Bravo pronašao si slovo! Tvoja reč izgleda ovako _ _ _ _ _ b _ b _
# # itd. itd.
# # Odlično! Pogodio si reč smrdibuba. Uspeo si to iz 20 pokušaja.
#
# Eleventh Task
# We will make a gallows game, example here -> http://www.losprimjer.com/vjesanje.php
# Of course ours will be a little different ...
# Define the word that the user needs to guess as a string, e.g. word_for_guess = 'smrdibuba'
# The user has an unlimited number of attempts
# Each time a user enters a letter, they should say if they hit a letter and print out parts of the word they have hit so far
# When a user guesses a word, it should print how many attempts it took to guess the word
# Example
# program: Imagined a word. Type a letter and try to guess the word (the correct word is smrdibuba)
# user: b
# program: Bravo you found the letter! Your word looks like this _ _ _ _ _ b _ b _
# etc. etc.
# Great! You guessed the word smrdibuba. You did it in 20 attempts.

word_for_guess = 'test'
list_word = list(word_for_guess)
attempt = 0
output_list = ['-' for x in list_word]

while list_word != output_list:
    input_letter = input('Imagined a word. Type a letter and try to guess the word.\n')
    for x in range(0, len(list_word)) :
        if list_word[x] == (input_letter) :
            output_list [x] = input_letter
            output_word = ' '.join(output_list)
    print('Bravo you found the letter! Your word looks like this {}'.format(output_word))
    attempt += 1

print('Great! You guessed the word {}. You did it in {} attempts.'.format(word_for_guess, attempt))
