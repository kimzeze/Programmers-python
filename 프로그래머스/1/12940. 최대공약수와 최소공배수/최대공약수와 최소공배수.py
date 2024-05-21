def solution(n, m):
    answer = []
    
    min_num = min(n,m)
    
    for i in range(min_num, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

            
    answer.append((n * m) // answer[0])
    
    return answer