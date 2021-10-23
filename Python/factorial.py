# Python Program to find factorial of a number.
# Using Recursion

def recur_factorial(n): 

    if n == 1: 
        return n 
    else: 
        return n*recur_factorial(n-1)
print(recur_factorial(5))

#Normal way

num = int(input("Enter a number: ") )
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1,int(num)+1):
        factorial = factorial * i
print("Factorail of ",num , " is : ",factorial)