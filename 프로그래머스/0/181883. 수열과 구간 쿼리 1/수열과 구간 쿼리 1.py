def solution(arr, queries):
    # arr = [0, 1, 2, 3, 4]
    # queries = [[0, 1], [1, 2], [2, 4]]
    
    for s, e in queries:
        # 첫 번째 쿼리: s = 0, e = 1
        # 두 번째 쿼리: s = 1, e = 2
        # 세 번째 쿼리: s = 2, e = 4
        
        for i in range(s, e + 1):
            # 첫 번째 쿼리:
            #   i = 0, arr[0] += 1, arr = [1, 1, 2, 3, 4]
            #   i = 1, arr[1] += 1, arr = [1, 2, 2, 3, 4]
            
            # 두 번째 쿼리:
            #   i = 1, arr[1] += 1, arr = [1, 3, 2, 3, 4]
            #   i = 2, arr[2] += 1, arr = [1, 3, 3, 3, 4]
            
            # 세 번째 쿼리:
            #   i = 2, arr[2] += 1, arr = [1, 3, 4, 3, 4]
            #   i = 3, arr[3] += 1, arr = [1, 3, 4, 4, 4]
            #   i = 4, arr[4] += 1, arr = [1, 3, 4, 4, 5]
            
            arr[i] += 1
    
    return arr
    # 최종 결과: [1, 3, 4, 4, 5]