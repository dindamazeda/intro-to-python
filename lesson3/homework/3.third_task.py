# TREĆI ZADATAK
# Dat je niz imenica u nasumičnom redosledu.
# Napisati program koji će da grupiše imenice u novu listu na osnovu početnog slova tj. da ih poređa po redosledu
# Međutim ima jedan uslov - prve imenice u novoj listi moraju da počinju sa slovom 'm', a nakon toga treba da ide po alfabetu
# Videti primer ispod
# ## primer ###
# imenice = ['patka', 'kvaka', 'staka', 'barka', 'marka', 'koka', 'ljorka', 'abrakadabra', 'mantra', 'karma', 'deka', 'seka', 'mleka']
# program: ['mantra', 'marka', 'mleka', 'abrakadabra', 'barka', 'deka', 'karma', 'koka', 'kvaka', 'ljorka', 'patka', 'seka', 'staka' ]
#
# Third Task
# a list of words in random is given.
# Write a program that group the words into a new list based on the initial letter. to sort them in order
# However, there is one condition - the first nouns in the new list must start with the letter 'm', and after that it should go in alphabetical order
# See example below
# Example
# nouns = ['patka', 'kvaka', 'staka', 'barka', 'marka', 'koka', 'ljorka', 'abrakadabra', 'mantra', 'karma', 'deka', 'seka', 'mleka']
# program: ['mantra', 'marka', 'mleka', 'abrakadabra', 'barka', 'deka', 'karma', 'koka', 'kvaka', 'ljorka', 'patka', 'seka', 'staka' ]


words = ['patka', 'kvaka', 'staka', 'barka', 'marka', 'koka', 'ljorka', 'mantra', 'karma', 'deka', 'seka', 'mleka']
sorted_words = sorted(words)

m_words =[]
no_m_words = []
for x in sorted_words:
    if x[0][0]=='m':
        m_words.append(x)
    else:
        no_m_words.append(x)

final_words = []
final_words.extend(m_words)
final_words.extend(no_m_words)

print(final_words)
