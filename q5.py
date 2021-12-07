# Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.


digit=int(input("Enter digit:"))
num=input("enter a number:")


result=0
for i in range(1,digit+1):
  result= result + int(str(num*i))
  print(num*i)

print("________________+\n")
print(result)

# Outout
# Enter digit: 3
# enter a number: 2
# 2
# 22
# 222
# ________________+

# 246
