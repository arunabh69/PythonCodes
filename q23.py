n=int(input("Enter any number :"))
t=n
reverse_n=0
while(n>0):
    d=n%10
    reverse_n=reverse_n*10+d
    n=n//10
if(t==reverse_n):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
