import math
from decimal import *

# For this final challenge, I tried two different approaches

def findSum(n):
    setcontext(Context(prec=2000, Emax=9999999999))
    ctx = getcontext()
    n1 = ctx.multiply(n,ctx.add(n,1))
    return Decimal(int(ctx.divide(n1,2)))

def findHihestElement(n):
    setcontext(Context(prec=2000, Emax=9999999999))
    ctx = getcontext()
    nSquare = ctx.power(n,2)
    newValue = ctx.multiply(nSquare, 2)
    value = ctx.sqrt(Decimal(newValue))
    return Decimal(int(value))

def findBigJ(n):
    setcontext(Context(prec=2000, Emax=9999999999))
    ctx = getcontext()
    value = ctx.multiply((ctx.sqrt(2)-1), n)
    svalue = str(value).split(".")[0]
    return Decimal(svalue)

# First solution

def solution(str_n):
    
    n = Decimal(str_n)
    
    setcontext(Context(prec=2000, Emax=9999999999))
    ctx = getcontext()

    allSums = []
    while n > 0:

        highV = findHihestElement(n)
        sumV = findSum(highV)
        bigJ = findBigJ(n)

        sumToSub = ctx.multiply(2,findSum(bigJ))
        allSums.append(int(ctx.subtract(sumV,sumToSub)))

        n = bigJ

    allSums.reverse()

    while len(allSums) > 1:
        allSums[0] = ctx.subtract(allSums[1], allSums[0])
        allSums.pop(1)
        
    return str(allSums[0])

# Second solution

def solution_2(n):
    
    setcontext(Context(prec=2000, Emax=9999999999))
    ctx = getcontext()

    n = int(n)

    allSums = []
    
    while n > 0:
        n2 = int(ctx.multiply((ctx.sqrt(2)-1),n))
        nn = ctx.multiply(n, n2)
        v = nn + findSum(n) - findSum(n2)
        allSums.append(v)
        n = n2

    while len(allSums) > 1:
        allSums[0] = allSums[1] - allSums[0]
        allSums.pop(1)
        
    s = str(allSums[0])
    return s



# print(solution_2("77"))
# print(solution_2("5"))

print(solution("77"))
print(solution("5"))








# NOTATIONS ONLY

# ========================================= 105 - 10 - 12
# 70710678118654752440084436210484903928483593768847403658833986899536623923105351942519376716382078624679624499680139607237798181744046467783846697970256425687262443342712887327254803273119967464820709
# 70710678118654752440084436210484903928483593768847403658833986899536623923105351942519376716382078624679624499680139607237798181744046467783846697970256425687262443342712887327254803273119967464820709
# 70710678118654752440084436210484903928483593768847403658833986899536623923105351942519376716382078624679624499680139607237798181744046467783846697970256425687262443342712887327254803273119967464820709
# 70710678118654752440084436210484903928483593768847403658833986899536623923105351942519376716382078624679624499680139607237798181744046467783846697970256425687262443342712887327254803273119967464820709
# Value: 10
# Recursive result: 73
# Integers found: [1, 2, 4, 5, 7, 8, 9, 11, 12, 14]
# Highest value = 14
# total sum of 14 = 105

# Manually found [3, 6, 10, 13], using solution_plus2 in 4.
# BigJ = 4
# Sum of these integers = 32

# 105 - 32 = 73

# ====

# Value: 77
# Recursive result: 4208
# Integers found: [1, 2, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 18, 19, 
# 21, 22, 24, 25, 26, 28, 29, 31, 32, 33, 35, 36, 38, 39, 41, 42, 43, 
# 45, 46, 48, 49, 50, 52, 53, 55, 56, 57, 59, 60, 62, 63, 65, 66, 67, 
# 69, 70, 72, 73, 74, 76, 77, 79, 80, 82, 83, 84, 86, 87, 89, 90, 91, 
# 93, 94, 96, 97, 98, 100, 101, 103, 104, 106, 107, 108]
# Highest value = 108
# total sum of 108 = 5886

# Manually found [3, 6, 10, 13, 17, 20, 23, 27, 30, 34, 37, 40, 44, 47, 
# 51, 54, 58, 61, 64, 68, 71, 75, 78, 81, 85, 88, 92, 95, 99, 102, 105]
# , using solution_plus2 in 31.
# BigJ = 31
# Sum of these integers = 1678

# 5886 - 1678 = 4208

# =========================================
