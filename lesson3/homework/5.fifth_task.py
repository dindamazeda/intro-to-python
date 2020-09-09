# PETI ZADATAK
# # Data je lista sa nekim stringovima, napisati program koji će da kaže kolika je frekventnost elemenata u listi tj. koliko puta se neki element ponavlaja u listi
# ### primer ###
# # imenice = ['abrakadabra', 'staka', 'marka', 'seka', 'patka', 'deka', 'mleka', 'marka', 'deka', 'deka', 'ljorka', 'staka', 'ljorka', 'staka', 'abrakadabra', 'mantra', 'staka', 'barka', 'ljorka', 'barka']
# # program: {'abrakadabra': 2, 'staka': 4, 'marka': 2, 'seka': 1, 'patka': 1, 'deka': 3, 'mleka': 1, 'ljorka': 3, 'mantra': 1, 'barka': 2}
#
# Fifth Task
# A list is given with some strings, write a program that will say how often the elements in the list are, i.e how many times an element is repeated in the list
# Example
# # words = ['abracadabra', 'staka', 'marka', 'seka', 'patka', 'deka', 'mleka', 'marka', 'deka', 'deka', 'ljorka', 'staka ',' ljorka ',' staka ',' abracadabra ',' mantra ',' staka ',' barka ',' ljorka ',' barka ']
# # program: {'abracadabra': 2, 'staka': 4, 'marka': 2, 'seka': 1, 'patka': 1, 'deka': 3, 'mleka': 1, 'ljorka': 3, 'mantra': 1, 'boat': 2}

import re

words = ['abracadabra', 'staka', 'marka', 'seka', 'patka', 'deka', 'mleka', 'marka', 'deka', 'deka', 'ljorka', 'staka ',' ljorka ',' staka ',' abracadabra ',' mantra ',' staka ',' barka ',' ljorka ',' barka ']
print(words)
frequency = {}

for x in words:
    x = re.sub(r"\s+", "", x, flags=re.UNICODE)
    # print(x)
    if x in frequency:
      frequency[x] += 1
    else:
      frequency[x] = 1

print(frequency)