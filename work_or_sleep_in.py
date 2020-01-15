#Prompts user for a day of the week, then decides between "going to work" or "sleeping in"

day = int(input("Day (0-6): "))

if(day == 1 or day == 6):
    print("Sleep in")
else:
    print("Go to work")