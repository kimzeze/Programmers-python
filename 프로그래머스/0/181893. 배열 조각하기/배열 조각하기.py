def solution(arr, query):
    answer = []
    for i in range(len(query)):
        index = query[i]
        # 짝수 인덱스이면
        if i % 2 == 0:
            arr = arr[:index+1]
        # 홀수 인덱스이면
        else:
            arr = arr[index:]
        
    return arr