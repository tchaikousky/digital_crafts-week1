# Will prompt the user for a number 0 to 6 inclusive, then print the day of the week that corresponds.

day = int(input("Enter a number (0-6): "))

if(day == 0):
    print("Sunday")
elif(day == 1):
    print("Monday")
elif(day == 2):
    print("Tuesday")
elif(day == 3):
    print("Wednesday")
elif(day == 4):
    print("Thursday")
elif(day == 5):
    print("Friday")
elif(day == 6):
    print("Saturday")
else:
    print("You did not enter a number between (0-6).")