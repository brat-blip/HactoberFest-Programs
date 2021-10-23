def smallestDivisor(n):
# if divisible by 2
    if (n % 2 == 0):
        return 2
    # iterate from 3 to sqrt(n)
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2
    return n
# Driver Code
n = int(input("Enter a number : "))
print(smallestDivisor(n))