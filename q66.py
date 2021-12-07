# Python program to delete an element from a list by index which is given by the user.

print(end="Enter the Size of List: ")
t = int(input())

arr = []
print(end="Enter " +str(t)+ " Elements: ")
for i in range(t):
    arr.append(input())

print(end="\nEnter the Index Number: ")
index = int(input())

if index<t:
    arr.pop(index)
    print("\nThe New list is: ")
    for i in range(t-1):
        print(end=arr[i]+" ")
else:
    print("\nInvalid Index Number!")
print()

# Output-
# Enter the Size of List: 5
# Enter 5 Elements: a
# b
# c
# d
# e
# Enter the Index Number: 3
# The New list is: 
# a b c e 
