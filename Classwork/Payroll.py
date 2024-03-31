# Amanda M
# 2/28/2024
# user enters pay rate & the hoursworked
# payrate within range $ 7.50 and $18.25 
# hours within range  of 0 and 40
# program displays the employee's gross pay

payRate = 0
hoursworked = 0
empgrosspay = 0

def payroll():
    global payRate
    payRate = (float(input('Enter the pay rate: ')))
    while payRate > 7.50 and payRate < 18.25:
        print(f'{payRate} is an accepted rate')
        return(payRate)
    else:
        print("Please input a correct pay rate.")
        payroll()
        
def hours():
    global hoursworked
    hoursworked = (float(input('Enter the hours worked: ')))
    while hoursworked > 0 and hoursworked < 40:
        print('Accepted hour limit.')
        return(hoursworked)      
    else: 
        print('Please input correct hours worked.')
        hours()

def calc():
    global empgrosspay    
    empgrosspay = payRate * hoursworked
    print(f"Your hours worked were {hoursworked}, your payrate is $16{payRate}, and your gross pay is ${empgrosspay}.")

payroll()
hours()
calc()
