def solution(arr):
    answer = []
    test = []
    
    if arr.count(2) == 0:
        answer.append(-1)
    elif arr.count(2) == 1:
        answer.append(2)
    
    for i in range(len(arr)):
        if arr[i] == 2:
            test = arr[i:]
            break
            
    for j in range(len(test)-1):
        if test[j+1] == 2:
            answer = test[:j+2]
        
    return answer