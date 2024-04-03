def solution(n, k):
    answer = []
    s = n // k
    for i in range(1, s+1):
        answer.append(i * k)
    return answer