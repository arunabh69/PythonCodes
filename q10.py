# A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.

unit = int(input())
cost = unit * 100
if cost > 10000:
    print(10000/2)
else:
    print(cost)
