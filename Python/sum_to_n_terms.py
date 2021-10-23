# Sum to N terms
n = int(input("Enter the number of terms : "))
#initialising sum to 0
sum = 0
#loop
for i in range (n+1):
    sum += i
print(sum)