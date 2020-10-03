# Date su dve liste. Napraviti dictionary gde će ključevi biti elementi prve liste, a vrednost elementi druge liste

list_of_position = ['pekar', 'mlekar', 'lekar', 'apotekar']
list_of_salary = [35000, 30000, 100000, 65000]

dictionary_combined = {position: salary for position, salary in zip(list_of_position, list_of_salary)}

print(dictionary_combined)