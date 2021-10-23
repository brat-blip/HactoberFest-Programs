# Number Palindrome
num1 = int(input("Enter a 5 digit number : ") )
#reversing the number
num = num1 # cloning the number
rev_num = 0
while (num > 0):
    remainder = num % 10
    rev_num = (rev_num * 10) + remainder
    num = num // 10
print(rev_num)
#Checking if equal
if (num1 == rev_num):
    print("Yes the original and reversed numbers are equal.") 
else: 
    print("No the original and reversed numbers are not equal.")
print(num1)
print(rev_num)



# # using recursion
num1 = int(input("Enter a 5 digit number : ") )
rev_num =0
def rev(num):
    global rev_num
    if (num > 0):
        remainder = num % 10
        rev_num = (rev_num * 10) + remainder
        rev(num // 10)
    return rev_num
print(rev(num1))