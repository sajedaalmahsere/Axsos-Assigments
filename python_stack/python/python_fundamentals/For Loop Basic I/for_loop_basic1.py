for int in range(0,151,1):
    print(int)

# -----------------------------------------------------

for i in range(5,1001,5):
    print(i)

#---------------------------------------------------------

for x in range(1,101,1):
    if(x % 10 == 0):
        print("Coding")
    elif(x % 5 == 0):
        print("Coding Dojo")
    else: print(x)

#-------------------------------------------------------

sum=0
for x in range(500001):
    if(x % 2 == 0):
        sum += x
print (sum)

#-------------------------------------------------------
for year in range(2018,0,-4):
    print(year)

# --------------------------------------------------------

lowNum = 1
highNum =26
mult= 10

for y in range(lowNum,highNum,1):
    if (y % mult == 0):
        print(y)