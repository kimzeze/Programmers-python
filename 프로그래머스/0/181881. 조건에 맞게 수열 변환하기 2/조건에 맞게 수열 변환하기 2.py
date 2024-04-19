def solution(arr):
    answer = 0
    prev_arr = arr[:]  # 이전 상태의 arr 저장
    
    while True:
        for i in range(len(arr)):
            # 50보다 크거나 같고 짝수이면
            if arr[i] >= 50 and arr[i] % 2 == 0:
                # 조건 1 실행
                arr[i] = arr[i] // 2
            # 50보다 작고 홀수이면
            elif arr[i] < 50 and arr[i] % 2 == 1:
                # 조건 2 실행
                arr[i] = arr[i] * 2 + 1
        
        answer += 1  # 반복 횟수 증가
        
        if arr == prev_arr:  # 현재 arr과 이전 arr이 같으면 반복 종료
            break
        
        prev_arr = arr[:]  # 현재 arr을 이전 arr로 저장
    
    return answer-1