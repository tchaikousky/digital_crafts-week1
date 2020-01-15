#Calculates the tip % and produces the total

bill_amount = int(input("Total bill amount? "))
service_level = input("Level of service? ('good', 'fair', 'bad')" ).lower()

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