
# for i in range(5,0,-1):
#     print (i) 
def count(number):
    for i in range(number,0,-1):
        print(i)
count(3)

# ---------------------------------------------------------

def twonumbers(num1):
    print(num1[0])
    return num1[1]
twonumbers([26,9])

# ---------------------------------------------------------

def plus(list):
    sum = list[0] + len(list)
    return sum
print(plus([1,2,3,4]))

# ------------------------------------------------------------

def greater(list):
    for i in range(len(list)):
        if(i>list[i]):
            return list[i]
        else:
            return False
        
# ---------------------------------------------------------------

def length_and_value(size, value):
    return [value] * size
print(length_and_value(2,9))