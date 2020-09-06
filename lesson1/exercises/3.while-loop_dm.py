# Write a program which will ask the user what is his favourite programming language is
# Continue asking the same question until the user enters 'Python'
### example ###
# program: What is your favourite programming language?
# user: Java
# program: What is your favourite programming language?
# user: C++
# program: What is your favourite programming language?
# user: Python
# program: That is the correct answer!


# This is a way to get user input

user_input = input('What is your favourite programming language? ')
answer = True
while answer:
    print(user_input)
    if user_input == 'Python':
        answer = False
        print('That is the correct answer')
    else:
        user_input = input('What is your favourite programming language? ')
