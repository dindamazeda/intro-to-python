#
# SEDMI ZADATAK
# # Enigma je mašina koja je korišćena za šifrovanje poruka -> https://en.wikipedia.org/wiki/Enigma_machine
# # Napisati program koji pita korisnika da otkuca neki tekst a zatim šifruje tu poruku i isprinta je
# # Šifrovanje je proces pretvaranja običnog teksta u neki nečitljiv tekst npr. tekst dobar dan pretvorimo u -> whkyi knq
# # Naš algoritam za šifrovanje će biti sledeći:
# # Imamo abecedu -> a,b,c,č,ć,d,dž,đ,e itd. -> https://sh.wikipedia.org/wiki/%C5%A0ablon:Srpskohrvatska_abeceda
# # Svako slovo iz korisnikovog teksta treba da se 'pomeri' za 4 mesta unapred u abecedi
# # Tako će npr. a postati ć, dok će b postati d itd.
# # Na taj način ćemo šifrovati poruku i ona će postati nečitljiva
# ### primer ###
# # program: Unesi neku reč ili neki tekst i ja ću da ti šifrujem taj tekst
# # korisnik: baba
# # program: Tvoja šifrovana poruka je dćdć
#
# Seventh Task
# Enigma is a machine used to encrypt messages -> https://en.wikipedia.org/wiki/Enigma_machine
# Write a program that asks the user to type some text and then encrypt that message and print it out
# Encryption is the process of converting plain text into some unreadable text eg text "good day" we convert to -> "whkyi knq"
# Our encryption algorithm will be as follows:
# We have the alphabet -> a, b, c, č, ć, d, dž, đ, e, etc. -> https://sh.wikipedia.org/wiki/%C5%A0ablon:Srpskohrvatska_abeceda
# Each letter in the user's text should be 'moved' 4 places forward in the alphabet
# Thus, for example, a will become ć, while b will become d, and so on.
# This way we will encrypt the message and it will become unreadable
# Example
# program: Enter a word or a text and I will encrypt that text for you
# user: baba
# program: Your encrypted message is djdc
import string

list_alphabet = list(string.ascii_lowercase)
input_word = input('Enter a word or a text and I will encrypt that text for you\n')

index_word = [list_alphabet.index(x) for x in input_word]
# print(index_word)

index_encrypted = []
encrypted_list = []


for x in index_word:
    if x > 21:
        x -= 20
    else:
        x += 4
    index_encrypted.append(x)
    encrypted_list.append(list_alphabet[x])

encrypted_string = ' '.join(encrypted_list)

print('Your encrypted message is {}'.format(encrypted_string))
