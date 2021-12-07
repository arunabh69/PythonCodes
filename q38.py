# Write a Python program to change a given string to a new string where the second and last chars have been exchanged.

string = input("Enter a string :-")
new_str = string[0] + string[-1] + string[2:-1] + string[1]
print(new_str)
