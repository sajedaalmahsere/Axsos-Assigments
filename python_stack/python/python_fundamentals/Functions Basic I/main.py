#1
def a():
    return 5
print(a()) #my prediction 5

# -------------------------------------------------------
#2
def a():
    return 5
print(a()+a()) #my prediction 10

# --------------------------------------------------------

#3
def a():
    return 5
    return 10 #unreachable code
print(a())  #my prediction 5

# ---------------------------------------------------------

#4
def a():
    return 5 #return ends the function emediatly
    print(10)
print(a()) #my prediction is 5 then print 10 but then I know the explaination

# ----------------------------------------------------------

#5
def a():
    print(5)
x = a() #function without return automatically returns None.
print(x) #my prediction 5 but then I know the explaination

#-----------------------------------------------------------

# #6
# def a(b,c):
#     print(b+c)  
# print(a(1,2) + a(2,3))  #my prediction is 8 but then I know the explaination

# a(1,2)=3 , a(2,3)=5 it does not have return so the value is None . None + None = TypeError

#----------------------------------------------------------

#7
def a(b,c):
    return str(b)+str(c) 
print(a(2,5)) #my prediction is 25
#str converts the int into string so the process happend concatination

# ----------------------------------------------------------

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) #my prediction is 100 , 10

# ---------------------------------------------------------

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #my prediction is 7
print(a(5,3)) #my prediction is 14
print(a(2,3) + a(5,3)) #my prediction is 21

# ---------------------------------------------------------

#10
def a(b,c):
    return b+c #my prediction is 8
    return 10
print(a(3,5))

# --------------------------------------------------------------

# #11
# b = 500
# print(b)
# def a():
#     b = 300 
#     print(b)
# print(b) #for the global variable that is 500
# a() # like we return the function and the value is 300
# print(b)

# #my prediction is 500, 300, 500 , 300, 500
# -----------------------------------------------------------------

#12
b = 500
print(b) #my prediction is 500
def a():
    b = 300
    print(b)
    return b #my prediction is 300 ,, 
# but the returned value 300 is not printed, because you didn't put print() around a().
print(b) #my prediction is 500
a() #my prediction is 300
print(b) #my prediction is 500

# ---------------------------------------------------------------------

#13
b = 500
print(b) #my prediction is 500
def a():
    b = 300
    print(b)
    return b
print(b) #my prediction is 500
b=a() #my prediction is 300
print(b) #my prediction is 300

# ------------------------------------------------------------------------

#14
def a():
    print(1) #my prediction is 1
    b()
    print(2) #my prediction is 2
def b():
    print(3) #my prediction is 3
a()  #my prediction is 2

#When one function calls another function, Python pauses the first function, runs the second one, then comes back to the first.

# ---------------------------------------------------------------------------

#15
def a():
    print(1) #my prediction is 1
    x = b() 
    print(x) #my prediction is 3 , 5
    return 10 
def b():
    print(3) 
    return 5
y = a() 
print(y) #my prediction is 10