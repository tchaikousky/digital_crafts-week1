#Prompts user for degrees in celsius and converts to fahrenheit

temp = int(input("What is the temperature in celsius? "))
conversion = (temp * 1.8) + 32
print(str(conversion) + " F")