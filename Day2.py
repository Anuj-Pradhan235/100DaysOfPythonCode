# Tip Calculator
print("Welcome to the tip calculator");
amount=float(input("What was the total bill? $"));
noOfPersons=int(input("How many people to split the bill? "));
tip=int(input("What percentage tip would you like to give? 10,12, or 15? "));
roundOfAmount=((amount+amount*(tip/100))/noOfPersons);
print("Each person should pay: $"+ str( round( roundOfAmount,2)))