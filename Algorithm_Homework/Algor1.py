# Amanda M
# Algorithm Workbench 1
# 2/13/2024

def bigUps():
    showTime = float(input("Enter a number to be multiplied: "))
    product = showTime * 10
    while product < 100:
        print(product)
        print(f"The product of {showTime} times 10 is {product}.")
        product = product + 10

bigUps()
