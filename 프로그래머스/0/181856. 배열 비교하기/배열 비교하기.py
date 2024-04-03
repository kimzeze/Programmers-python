def solution(arr1, arr2):
    sumArr1 = 0
    sumArr2 = 0
    
    if len(arr1) == len(arr2):
        for i in arr1:
            sumArr1 += i
        for j in arr2:
            sumArr2 += j
        if (sumArr1 > sumArr2):
            return 1
        elif (sumArr1 == sumArr2):
            return 0
        else :
            return -1
    elif len(arr1) > len(arr2):
        return 1
    else :
        return -1