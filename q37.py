# "Write a Python program to count the number of characters (character frequency) in a string. 
#  Sample String : google.com'
#  Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"

str1 =  input()
def char_frequency (str1):
    dict = {}
    for n in str1 :
        keys = dict.keys ()
        if n in keys :
            dict[n] += 1
        else :
            dict[n] = 1
    return dict

print (char_frequency(str1))

# Output-
# google.com
# {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
