birds = {'vrabac', 'orao', 'soko', 'papagaj', 'jastreb', 'ždral'}
birds.add('gavran')

print(birds)


egsotic_birds = {'pelikan', 'kondor', 'paun'}
birds.update(egsotic_birds)

print(birds)


immutable_birds = frozenset(birds)
print(immutable_birds)