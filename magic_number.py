#Prompt the user for a number and compare it to a predefined value

my_num = 10

user_input = input("Enter a number: ")

if(my_num == int(user_input)):
    print("Great guess")
else:
    print("Sorry, try again")