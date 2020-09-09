# DESETI ZADATAK
# # Fibonačijev niz - napisati program koji će da isprina Fibonačijev niz
# # Fibonačijev niz je niz gde je svaki sledeći element u nizu zbir dva prethodna broja iz zbira -> https://en.wikipedia.org/wiki/Fibonacci_number
# # Pošto Fibonačijev niz može da ide do beskraja, isprintati niz samo do broja 377 a onda prekinuti program
# ### primer ###
# # program: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
#
# Tenth Task
# Fibonacci sequence - write a program that will tell the Fibonacci sequence
# Fibonacci string is a string where each subsequent element in the string is the sum of two previous numbers from the sum -> https://en.wikipedia.org/wiki/Fibonacci_number
# Since the Fibonacci sequence can go on indefinitely, print the string only to number 377 and then abort the program
# Example
# program: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
#
list_fibonacci = [1,1]
x = 2
while x <=13:
    list_fibonacci.append(list_fibonacci[x-1]+list_fibonacci[x-2])
    x+=1
print(list_fibonacci)

