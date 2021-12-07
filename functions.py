x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)


#output
x inside: global
x outside: global
------------------------------------------

#Create a Local Variable

def foo():
    y = "local"
    print(y)

foo()

#output
local
-----------------------------------------

#Global and Local variables in the same code

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

#output
global global 
local

---------------------------------------------

#Create a nonlocal variable

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

#output
inner: nonlocal
outer: nonlocal
