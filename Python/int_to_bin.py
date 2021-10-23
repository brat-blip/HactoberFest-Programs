# Int to Binary
def binary(num):
    while (num > 0):
        temp = num % 2
        bin_no.append(temp)
        num = num // 2
bin_no = []   
n = int(input("Enter a number : "))
binary(n)
print("The binary of ",n," is ",end=" ")
for i in range (1,len(bin_no)+1):
        print(bin_no[-i],end="")