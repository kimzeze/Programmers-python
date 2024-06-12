def solution(n):
    answer = []
    for i in range(1, n):
        if n // i == (n/i):
            answer.append(i)
    answer.append(n)
    return answer