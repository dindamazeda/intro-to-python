birds = {'vrabac', 'orao', 'soko', 'papagaj', 'jastreb', 'ždral'}

birds.remove('soko')
print(birds)

# KeyError
# ptice.remove('pelikan')

birds.discard('pelikan')


some_bird = birds.pop()
print(some_bird)


birds.clear()
print(birds)