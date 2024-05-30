def solution(park, routes):
    # 가로
    col = len(park)
    
    # 세로
    row = len(park[0])
    
    # 현재 위치 초기화
    current = [0, 0]
    
    # 시작 위치 탐색
    for i in range(col):
        for j in range(row):
            if park[i][j] == 'S':
                current = [i, j]
                break
        if current != [0, 0]:
            break
    
    # 공원 크기
    park_length = [row, col]
    
    for route in routes:
        target = route.split()
        direction = target[0]
        move = int(target[1])
        
        # 이동 전 위치 저장
        before = current[:]
        
        for _ in range(move):
            if direction == 'E':
                current[1] += 1
            elif direction == 'W':
                current[1] -= 1
            elif direction == 'S':
                current[0] += 1
            elif direction == 'N':
                current[0] -= 1
            
            # 경계 체크
            if not (0 <= current[0] < col and 0 <= current[1] < row):
                current = before
                break
            
            # 장애물 체크
            if park[current[0]][current[1]] == 'X':
                current = before
                break
    
    return current
