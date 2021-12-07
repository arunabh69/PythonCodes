n=int(input("Enter a number:"))
i=1
while(n>0):
    dig=n%10
    i=i*dig
    n=n//10
print("The total sum of digits is:",i)
