def solution(line):
    # 깊은 복사를 방지하기 위한 초기화
    answer, pos = [], []  # 교점을 저장할 리스트 초기화
    n = len(line)  # 주어진 직선의 개수 계산
    
    # 최소 및 최대 x, y 좌표값을 저장할 변수 초기화 (매우 큰/작은 값으로 초기화하여 비교 가능하게 함)
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    for i in range(n):
        a, b, e = line[i]  # i번째 직선의 계수 (a, b, e)
        for j in range(i+1, n):
            c, d, f = line[j]  # j번째 직선의 계수 (c, d, f)
            # 두 직선이 평행하거나 일치하는 경우 계산하지 않고 건너뜀
            if a * d == b * c: continue
            # 두 직선의 교점 (x, y) 계산
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            # 계산된 교점이 정수인 경우만 처리
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])  # 계산된 교점을 pos 리스트에 추가
                # 최소 및 최대 x, y 좌표값 업데이트
                if x_min > x: x_min = x
                if y_min > y: y_min = y
                if x_max < x: x_max = x
                if y_max < y: y_max = y
                
    # 그리드의 크기 계산 (최소/최대 좌표값을 이용)
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    # 그리드 초기화 (모든 값을 '.'로 설정)
    coord = [['.'] * x_len for _ in range(y_len)]

    # 교점의 위치에 '*' 표시
    for star_x, star_y in pos:
        nx = star_x - x_min  # 교점의 x 좌표를 그리드에 맞게 조정
        ny = star_y - y_min  # 교점의 y 좌표를 그리드에 맞게 조정
        coord[ny][nx] = '*'  # 조정된 좌표 위치에 '*' 표시
        
    # 그리드의 각 행을 문자열로 변환하여 answer 리스트에 추가
    for result in coord: answer.append(''.join(result))
    
    # 최종 결과를 y축 방향으로 뒤집어서 반환
    return answer[::-1]
