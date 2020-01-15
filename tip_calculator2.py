#Calculates total including tip and give the option to divide total amount

bill_amount = int(input("Total bill amount? "))
service_level = input("Level of service? ('good', 'fair', 'bad') " ).lower()
split = int(input("Split how many ways? "))
flag = True

if(service_level == "good"):
    tip = bill_amount * .2
    total = tip + bill_amount
    print("Tip amount: " + str(tip))
    print("Total amount: " + str(total))
elif(service_level == "fair"):
    tip = bill_amount * .15
    total = tip + bill_amount
    print("Tip amount: " + str(tip))
    print("Total amount: " + str(total))
elif(service_level == "bad"):
    tip = bill_amount * .10
    total = tip + bill_amount
    print("Tip amount: " + str(tip))
    print("Total amount: " + str(total))
else:
    print("Service level not recognized.")
    flag = False

if(flag):
    print("Amount per person: " + str(total/split))