# Data je lista brojeva. Proći kroz niz i sabrati svaki element sa njegovim indeksom a zatim sve to podići na treći stepen (na kub)
# Isprintati listu sa novim brojevima na kraju

list_of_numbers = [153, 74, 196, 249, 33, 51, 229, 7, 227, 211, 133, 65, 118, 195, 4, 167, 250, 43, 253, 31, 159, 113,
                   59, 188, 72, 5, 113, 89, 83, 103, 2, 35]
#
# new_list = []
# for index, number in enumerate(list_of_numbers):
#     new_list.append((number+index)**3)
#     # print(index,number)


new_list = [((number+index)**3) for index, number in enumerate(list_of_numbers)]
print(new_list)


