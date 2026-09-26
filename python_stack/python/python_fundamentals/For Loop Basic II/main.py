def biggie_size(big):
    for i in range(len(big)):
        if (big[i]>-1):
            big[i] = ("big")
        else:
            continue
    return big
# print(biggie_size([-5,9,7,-3]))

# ---------------------------------------------------------------------

def count_positives(positive):
    count = 0
    for i in range(len(positive)):
        if positive[i]> 0:
            count += 1
        else:
            continue
    positive[len(positive) - 1] = count
    return positive
# print(count_positives(positive=[-5,9,7,8,7,-3]))

# ----------------------------------------------------------------------

def sum_total(diget):
    sum = 0
    for i in range(len(diget)):
        sum += diget[i]
    return sum
# print(sum_total([1,2,4]))

# -------------------------------------------------------------------------

def average(avg):
    sum = 0
    averg = 0
    for x in range(len(avg)):
        sum += avg[x]
        averg = sum  / len(avg)
    return averg
# print(average([2,3,4,5]))

# ---------------------------------------------------------------------------

def length(index):
    sum = 0
    for i in range(len(index)):
        sum = 1 + i
    return sum
# print(length([]))

# -----------------------------------------------------------------------------

def minimum(value):
    if len(value) == 0:
        return False
    
    min = value[0]
    for i in range(len(value)):
        if min > value[i]:
            min = value[i]
    return min
# print(minimum([4,6,8,3]))

# --------------------------------------------------------------------------------

def maximum(value):
    if len(value) == 0:
        return False
    
    max = value[0]
    for i in range(len(value)):
        if max < value[i]:
            max = value[i]
    return max
# print(maximum([4,6,8,3]))

# ---------------------------------------------------------------------------------

def ultimate_analysis(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for i in range(len(numbers)):
        total += numbers[i]

        if minimum > numbers[i]:
            minimum = numbers[i]
        if maximum < numbers[i]:
            maximum = numbers[i]
    average = total / len(numbers)
    length = len(numbers)

    print("sumTotal:", total)
    print("average:", average)
    print("minimum:", minimum)
    print("maximum:", maximum)
    print("length:", length)
# ultimate_analysis([37, 2, 1, -9])

# --------------------------------------------------------------------------

def reverse_list(list):
    right = len(list)-1
    left = 0
    while left < right:
        number = list[left]
        list[left] = list[right]
        list[right] = number

        left += 1
        right -=1
    return list
print(reverse_list([1,2,3,4,5]))
        
