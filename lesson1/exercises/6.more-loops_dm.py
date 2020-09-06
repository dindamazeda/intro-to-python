# write a loop that will sum up all numbers from 1 to 100 and print out the result
### example ###
# expected result -> 5050

sum = 0
for numbers in range(1, 101):
    sum = sum + numbers
print(sum)

# with the help of for loop triple each number from this list and print out the result
numbers = [5, 25, 66, 3, 100, 34]

for number in numbers:
    triple = number * 3
    print(triple)

# with the help of for loop and range() function print out all odd numbers from 1 to 100
### example ###
# program: 1, 3, 5, 7 etc.

for numbers in range(1, 101):
    if numbers % 2 == 0:
        continue
    print(numbers)
