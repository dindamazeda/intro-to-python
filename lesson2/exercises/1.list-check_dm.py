# Rewrite this program to perform the same check but with using a list instead

color = input("(blue, yellow, red). Input one of these colors.\n")

# if color == 'red':
#     print('Roses are red')
# elif color == 'yellow':
#     print('Sunflowers are yellow')
# elif color == 'blue':
#     print('Blue jasmine')
# else:
#     print('You haven\'t entered the proper color!!!')

color_list = ['blue', 'yellow', 'red']


if color == color_list[0]:
    print('Blue jasmine')
elif color == color_list[1]:
    print('Sunflowers are yellow')
elif color == color_list[2]:
    print('Roses are red')
else:
    print('You haven\'t entered the proper color!!!')