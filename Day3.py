#Coditional Statement
# print("Welcome to Rollercoaster!")
# height=int(input("What is your height in cm? "))
# if(height>120):
#     print("Can ride")
# else :
#     print("Can't ride")

#Odd or Even
# number=int(input("Enter the number:"));
# if(number%2==0):
#     print("The given number is even");
# else:
#     print("The given number is odd");

#Nested if/else statment
height_in_cm=int(input("Enter your height: "));
age=int(input("Enter your age: "));
if(height_in_cm>120):
    print("Can ride")
    if(age<=18):
        print("You have to pay $7")
    else:
        print("You have to pay $12")    
else:
    print("Can't ride")