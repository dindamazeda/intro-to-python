# Dat je niz imenica. Napisati program koji će da grupiše imenice u novu listu na osnovu početnog slova
# we have a list of words. Write a program that will group these words into a new list which is sorted by first letter
# There is one condition though - the first words in the new list should start with letter m
### example ###
# words = ['patka', 'kvaka', 'staka', 'barka', 'marka', 'koka', 'ljorka', 'mantra', 'karma', 'deka', 'seka', 'mleka']
# program: ['mantra', 'marka', 'mleka', 'barka', 'deka', 'karma', 'koka', 'kvaka', 'ljorka', 'patka', 'seka', 'staka' ]

words = ['patka', 'kvaka', 'staka', 'barka', 'marka', 'koka', 'ljorka', 'mantra', 'karma', 'deka', 'seka', 'mleka']
# words.sort()
# sorted_words = sorted(words)
# print(sorted_words)

m_words =[]
no_m_words = []
for x in words:
    if x[0][0]=='m':
        m_words.append(x)
    else:
        no_m_words.append(x)

sorted_m_words = sorted(m_words)
sorted_no_m_words = sorted(no_m_words)
print(m_words)
print(no_m_words)

final_words = []
final_words.extend(sorted_m_words)
final_words.extend(sorted_no_m_words)

print(final_words)
