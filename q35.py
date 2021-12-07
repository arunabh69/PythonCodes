# "Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string.
#  Sample String : 'abc', 'xyz' 
#  Expected Result : 'xbc ayz'"


a=input()

b=input()

x=a[0:1]

a=a.replace(a[0:1],b[0:1])

b=b.replace(b[0:1],x)

print(a,b)

# Output-
# abc
# xyz
# xbc ayz
