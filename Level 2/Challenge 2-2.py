# Function to change base
def changeBase(n, b):
    if n == 0:
        return 0
    digits = ""
    while n:
        digits += str(n % b)
        n //= b
    return digits[::-1]

# solution
def solution(n, b):
    
    # k is the lenght of n
    k = len(n)
    
    # Transform the string n in list of chars
    listIntRegular = []
    listIntRegular[:0] = n
    
    # Find a descending List of chars
    listIntRegular.sort(reverse = True)
    listIntDescending = list(listIntRegular)
    
    # Find a ascending List of chars
    listIntRegular.sort()
    listIntAscending = list(listIntRegular)
    
    # Trasnform the lists of chars in string again
    stringAsc = ""
    stringDes = ""
    for i in listIntAscending:
        stringAsc += i
    for i in listIntDescending:
        stringDes += i

    # Calculating Z from numbers in base 10
    z = int(stringDes, b) - int(stringAsc, b)
    # Transforming Z back to string
    z = changeBase(z,b) # transform back to the base b

    # Fill with zeroes if lenght less than k
    listInt = []
    listInt[:0] = str(z)
    while(len(listInt) < k):
        listInt.insert(0,'0')

    # Generating a string from the list of ints
    fullstring = "";
    for i in listInt:
        fullstring += i
    
    # If already contains this value in the total list, it reached a cycle
    if fullstring in globalIdList:
        # getting the substring that contains the repeating cycle only, and returning its lenght
        listRepeat = globalIdList[globalIdList.index(fullstring):]
        return len(listRepeat)
    else:
        globalIdList.append(fullstring)
        return solution(fullstring, b)


# global list that contains the ID
globalIdList = []

# Test 1
s = '210022'
s2 = 3

# Test 2
s = '1211'
s2 = 10

print(solution(s, s2))