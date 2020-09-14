numbers_list = [2, 3, 4, 5, 6, 7, 8]

# old way
squared_numbers_1 = []

for number in numbers_list:
    squared_numbers_1.append(number * number)

# new way
squared_numbers_2 = [number * number for number in numbers_list]

print(squared_numbers_1)
print(squared_numbers_2)
print(squared_numbers_1 == squared_numbers_2)

squared_numbers_divisible_by_2 = [number * number for number in numbers_list if number % 2 == 0]

print(squared_numbers_divisible_by_2)
