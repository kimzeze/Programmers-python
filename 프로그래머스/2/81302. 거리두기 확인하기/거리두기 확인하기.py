## ** 문제 4. 거리두기 확인하기 LEVEL-2 / page.93 **

def solution(places):
    answer = []  # 최종 결과를 저장할 리스트
    # 상하좌우 이동을 위한 배열
    # 이 배열들을 이용하여 현재 위치(j, k)에서 다음과 같이 이동할 수 있습니다:
		# 오른쪽 이동: (j + m1a[0], k + m1b[0]) -> (j, k+1)
		# 왼쪽 이동: (j + m1a[1], k + m1b[1]) -> (j, k-1)
		# 아래쪽 이동: (j + m1a[2], k + m1b[2]) -> (j+1, k)
		# 위쪽 이동: (j + m1a[3], k + m1b[3]) -> (j-1, k)
    m1a = [0, 0, 1, -1]  
    m1b = [1, -1, 0, 0]  

		
    # 대각선 포함, 한 칸 건너뛰어 이동을 위한 배열
    # 이 배열들을 이용하여 현재 위치(j, k)에서 다음과 같이 이동할 수 있습니다:
		# 상하좌우 2칸 이동: (j±2, k), (j, k±2) – 직선 방향으로 한 칸을 건너뛴 위치를 검사합니다.
		# 대각선 이동 및 인접: (j±1, k±1) – 대각선 방향으로 한 칸 떨어진 위치를 검사합니다.
    m2a = [2, -2, 0, 0, 1, 1, -1, -1]  
    m2b = [0, 0, 2, -2, -1, 1, -1, 1]  

    # places의 각 장소(5x5 행렬)에 대해 검사
    for i in range(5):
        current = places[i]  # 현재 장소 (대기실)
        result = 1  # 해당 장소(대기실)의 검사 결과, 초기값은 (1)로 설정
        for j in range(5):
            for k in range(5):
                # 현재 칸에 사람('P')이 있는 경우
                if(current[j][k] == "P"):
                
                
                
                    # case 1 -> 상하좌우 인접 칸 검사 (맨해튼거리 1인 경우)
                    for a in range(4):
                        d1a = j + m1a[a]
                        d1b = k + m1b[a]
                        # 배열 범위 내에 있을 때만 검사
                        if(-1 < d1a < 5 and -1 < d1b < 5):
                            # 인접 칸에도 사람('P')이 있는 경우, 거리두기 지침 위반
                            if(current[d1a][d1b] == "P"):
                                result = 0  # 지침 위반으로 표시
                                break  # 더 이상 검사할 필요 없음
                                
                                
                                
                    # case 2 -> 한 칸 건너뛰어 인접 칸 검사 (맨해튼거리 2인 경우)
                    for a in range(8):
                        d2a = j + m2a[a]
                        d2b = k + m2b[a]
                        # 배열 범위 내에 있을 때만 검사
                        if(-1 < d2a < 5 and -1 < d2b < 5):
                            # 한 칸 건너 인접 칸에 사람('P')이 있는 경우
                            if(current[d2a][d2b] == "P"):
                                # 직선 방향으로 한 칸 건너의 경우
                                if(abs(d2a - j) == 2):
                                    # 중간 칸이 빈 테이블('O')인 경우, 거리두기 지침 위반
                                    # 예를 들어, 한 'P'가 (2, 2)에 있고 다른 'P'가 (4, 2)에 있을 때, (4 + 2) // 2 = 3이므로, 사이 칸인 (3, 2)가 'O'(빈 테이블)인지 확인하는 것입니다.
                                    if(current[(d2a + j) // 2][d2b] == "O"):
                                        result = 0
                                        break
                                elif(abs(d2b - k) == 2):
                                    # 중간 칸이 빈 테이블('O')인 경우, 거리두기 지침 위반
                                    if(current[d2a][(d2b + k) // 2] == "O"):
                                        result = 0
                                        break
                                # 대각선 방향의 경우, 사이에 빈 테이블('O')이 하나라도 있는 경우 거리두기 지침 위반
                                elif(current[d2a][k] == "O" or current[j][d2b] == "O"):
                                    result = 0
                                    break
                    # 거리두기 지침 위반을 찾은 경우, 더 이상 검사할 필요 없이 반복문 탈출
                    if(result == 0):
                        break
                # 거리두기 지침 위반을 찾은 경우, 더 이상 검사할 필요 없이 반복문 탈출
                if(result == 0):
                        break
        # 현재 장소에 대한 검사 결과를 결과 리스트에 추가
        answer.append(result)

    return answer  # 모든 장소에 대한 검사 결과를 담은 리스트 반환