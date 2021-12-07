n = int(input("Enter any Number: "))
s = 0
t = n

while(t > 0):
    Factorial = 1
    i = 1
    Reminder = t % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\nFactorial of %d = %d" %(Reminder, Factorial))
    s = s + Factorial
    t = t // 10

print("\nSum of Factorials of a Given Number %d = %d" %(n, s))

if (s == n):
    print("%d is a Strong Number" %n)
else:
    print("%d is not a Strong Number" %n)]
