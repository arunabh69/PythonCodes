# Given two integer numbers return their sum. If the sum is greater than 100, then return their product.

def sum(num1, num2):
    sum = num1 + num2
    if sum <= 100:
        return sum
    else:
        return num1 *num2

result = sum(20, 30)
print("The result is", result)

result = sum(40, 90)
print("The result is", result)

# Output-
# The result is 50
# The result is 3600
