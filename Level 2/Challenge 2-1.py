
def solution(total_lambs):
    
    total_Lamb_spent_low = 0
    total_Lamb_spent_high = 0
    currentIndex = 0
    highLamb = []  
    lowLamb = []
    
    while (True):
        if (total_Lamb_spent_high < total_lambs):

            if (currentIndex > 0):
                newHighValue = highLamb[currentIndex-1] * 2
            else:
                newHighValue = 1

            total_Lamb_spent_high += newHighValue
            if (total_Lamb_spent_high <= total_lambs):
                highLamb.append(newHighValue)

        ## --------- LOW

        if (total_Lamb_spent_low < total_lambs):
            if (currentIndex > 1):
                newHighValue = lowLamb[currentIndex-2] + lowLamb[currentIndex-1]
            else:
                newHighValue = 1

            total_Lamb_spent_low += newHighValue
            if (total_Lamb_spent_low <= total_lambs):
                lowLamb.append(newHighValue)

        ## ---------- CHECK

        if (total_Lamb_spent_low >= total_lambs & total_Lamb_spent_high >= total_lambs):
            break

        currentIndex = currentIndex + 1

    return len(lowLamb) - len(highLamb)


s = 143 # Test 1
s = 10 # Test 2

print(solution(s))


