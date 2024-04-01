# Do - While loop but not possible in Python
# 2/14/2024
# Amanda M

keepGoing = "y"
def calcUlator():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a second number: "))
    sum = number1 + number2
    print(sum)

while keepGoing == "y":
    keepGoing = input("Do you want to add using the calcUlator? Enter y for yes, n for no. ")
    if keepGoing == "y":
        calcUlator()
    else:
        print("Happy Valentine's day!")
