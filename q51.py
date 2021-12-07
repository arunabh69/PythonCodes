# Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.


def middle(a, b, c) :
    return min(max(a,b),max(b,c),max(a,c))

a = int(input("Give a value: "))
b = int(input("Give b value: "))
c = int(input("Give c value: "))
print("The requested value is ")
print(middle(a,b,c)) 

# Output-
# Give a value: 18
# Give b value: 20
# Give c value: 8
# The requested value is 
# 18
