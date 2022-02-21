
def solution(num_buns, num_required):

    nOfElementsToDistribute = num_buns - (num_required - 1)
    totalNOfKeys = factorial(num_buns) / (factorial(nOfElementsToDistribute) * factorial(num_buns-nOfElementsToDistribute))

    listOfBunnies = []
    for i in range(num_buns):
        listOfBunnies.append(i)

    keys = Distribute(listOfBunnies, nOfElementsToDistribute)

    bunnies = {}
    for i in range(len(listOfBunnies)):
        bunnies[i] = []

    currentKey = -1
    for i in keys:
        currentKey += 1
        for u in i:
            bunnies[u].append(currentKey)

    distributedKeys = []

    for rr in bunnies:
        distributedKeys.append(bunnies[rr])
        
    return distributedKeys
        
def Distribute(lst, n):
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(lst)):
        m = lst[i]
        nLst = lst[i + 1:]
        for p in Distribute(nLst, n-1):
            l.append([m]+p)
    return l
    
def factorial(n):
    factorial = 1          
    for i in range(1,n + 1):    
       factorial = factorial*i    
    return factorial

# =========

# Test 1
print(solution(2, 1))

# Test 2
print(solution(5, 3))

