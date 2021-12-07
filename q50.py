# "Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
# "


string = 'Y-tatata-acropolis: 0.8475'

col_pos = string.find(':')                  
n = string[col_pos + 1:]               
a = float(n)                  
print(a)

# Output-
# 0.8475
