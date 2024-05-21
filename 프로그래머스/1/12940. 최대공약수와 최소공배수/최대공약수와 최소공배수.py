def solution(n, m):
    answer = []
    
    min_num = min(n,m)
    
    # n, m 을 나누어서 나머지가 0이 되는 가장 큰 값 => 최소공배수
    for i in range(min_num, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    
    # n * m 을 최대공약수로 나눈 값 => 최대공약수
    answer.append((n * m) // answer[0])
    
    return answer