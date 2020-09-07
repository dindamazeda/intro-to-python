# In the past 10 days we have recorded the daily temperature and stored it in a ordered list
# Turn this list into a dictionary where keys will be like day-1, day-2 etc. followed by a measurement for that day
### example ###
# temperature_by_day = [27, 25, 29, 27, 30, 25, 28]
# program: {day-1: 27, day-2: 25, day-3: 29 ....}

temperature_by_day = [27, 25, 29, 27, 30, 25, 28]
dictionary_temperature ={}
day = []
for x in range(0, len(temperature_by_day)):
    day.append('day-{}'.format(x + 1))
    dictionary_temperature[day[x]] = temperature_by_day[x]

print(dictionary_temperature)