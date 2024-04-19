def solution(arr, k):
    answer = []
    for target in arr:
        if target not in answer and len(answer) < k:
            answer.append(target)
    
    print(answer)
    print(len(answer))
    if len(answer) != k :
        for _ in range(k-len(answer)):
            answer.append(-1)
    return answer