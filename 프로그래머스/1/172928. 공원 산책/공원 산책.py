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
        # ex) ['E', '2']
        target = route.split()
        # 방향 저장
        direction = target[0]
        # 이동 크기 저장
        move = int(target[1])
        
        # 조건이 안맞을 때 초기화를 위해 이동 전 위치를 임시 저장
        before = current.copy()
        print(before)
        
        for _ in range(move):
            # 방향으로 1씩 추가
            if direction == 'E':
                current[1] += 1
            elif direction == 'W':
                current[1] -= 1
            elif direction == 'S':
                current[0] += 1
            elif direction == 'N':
                current[0] -= 1
            
            # 조건 1 : 공원 벗어났는지 체크해서 벗어났으면 초기화
            if not (0 <= current[0] < col and 0 <= current[1] < row):
                current = before
                break
            
            # 조건 2 : 현재 위치가 장애물 위치랑 같으면 초기화
            if park[current[0]][current[1]] == 'X':  
                current = before
                break
                
    return current
