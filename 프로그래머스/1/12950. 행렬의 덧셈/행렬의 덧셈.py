def solution(arr1, arr2):

    length_A = len(arr1)
    length_B = len(arr1[0])
    
    answer = [[] for _ in range(length_A)]  
    


    for i in range(length_A):
        for j in range(length_B):
            answer[i].append(0)
            

    
    for i in range(length_A):         
        for j in range(length_B):     
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer 

