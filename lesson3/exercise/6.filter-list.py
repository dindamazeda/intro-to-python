# write a program that will take 10 numbers from user input
# The program needs to go through these numbers and create a new list where the numbers which are greater than 10 and less than 20 are stored

index = []
filtered_number = []
unfiltered_number = []

for x in range(10):
    index.append(x)
    input_number= int(input('Enter number:'))
    if input_number > 10 and input_number < 20:
        filtered_number.append(input_number)
    else:
        unfiltered_number.append(input_number)

print(filtered_number)
