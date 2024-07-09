def solution(array, commands):
    answer = []
    cut = []
    
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1 
        
        cut = array[i:j]
        cut.sort()
        answer.append(cut[k])
        
    return answer