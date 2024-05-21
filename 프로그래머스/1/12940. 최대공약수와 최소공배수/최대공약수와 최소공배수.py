def solution(n, m):
    answer = []
    
    min_num = min(n,m)
    
    # n, m 을 나누어서 둘다 나머지가 0이 되는 가장 큰 값 => 최소공배수
    # (n, m)의 최솟값부터 시작해서 0까지 하나씩 나눠봄
    for i in range(min_num, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    
    # n * m 을 최대공약수로 나눈 값 => 최대공약수
    answer.append((n * m) // answer[0])
    
    return answer