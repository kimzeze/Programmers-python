def solution(n):
    answer = ''
    while n: 
        answer += str(n % 3) # 2) n으로 나눈 나머지를 answer에 추가
        n //= 3
        
    return int(answer, 3)