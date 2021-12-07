# 2.Program to demonstrate Tuple

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("Hi", [1, 3, 2], (9, 8, 7))
print(my_tuple)

# tuple unpacking 
my_tuple = 2, 1.2, "tiger"
print(my_tuple)

a, b, c = my_tuple

print(a)      
print(b)      
print(c)      

# tuple elements using indexing
my_tuple = ('a','b','c','d','e','f')

print(my_tuple[0])    
print(my_tuple[5])  
print(my_tuple[-1])


# nested tuple
x_tuple = ("tiger", [8, 4, 6], (1, 2, 3))

# nested index
print(x_tuple[0][3])       
print(x_tuple[1][1])   


# tuple elements using slicing
my_tuple = ('a','b','c','d','e','f')

print(my_tuple[1:4])
print(my_tuple[:-5])
print(my_tuple[5:])
print(my_tuple[:])
