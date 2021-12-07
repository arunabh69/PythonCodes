# "Write a Python program to add 'polis' at the end of a given string (length should be at least 3).
#   If the given string already ends with 'polis' then add 'polisCS' instead.
#   If the string length of the given string is less than 3, leave it unchanged. 
#  Sample String : 'abc'
#  Expected Result : 'abcpolisCS' 
#  Sample String : 'Acropolis'
#  Expected Result : 'AcropolisCS'"

str1=input()
def add_string(str1):
    if len(str1)<3:
        return str1
    if(str1.endswith('polis')):
        str1+="polisCS"
    else:
        str1+="polis"
    return str1


print(add_string(str1))


# Output-
# abc
# abcpolis
# Acropolis
# AcropolispolisCS
