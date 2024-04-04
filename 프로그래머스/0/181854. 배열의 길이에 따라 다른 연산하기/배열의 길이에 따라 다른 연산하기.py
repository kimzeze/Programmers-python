def solution(arr, n):
    answer = []
    for i in range(len(arr)):
        # 짝수인 경우
        if len(arr) % 2 == 0 and i % 2 == 1 :
            answer.append(arr[i]+n)
        elif len(arr) % 2 == 1 and i % 2 == 0 :
            answer.append(arr[i]+n)
        else:
            answer.append(arr[i])
            
    return answer