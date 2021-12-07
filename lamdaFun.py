# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(3))

--------------------------------------

# Program to double each item in a list using map()

my_list = [1, 3, 2, 4, 5, 6, 7, 8]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

---------------------------------------

#Program to show the use of lambda functions(reduce)

from functools import reduce
s = [1,2,3,4,5]
p= reduce (lambda x, y: x*y, s)
print(p)
