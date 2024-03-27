def rotate(x1, y1, x2, y2, matrix):
    # 회전의 시작 지점 값을 저장합니다.
    first = matrix[x1][y1]
    # 최소값을 찾기 위해 시작 지점의 값을 초기 최소값으로 설정합니다.
    min_value = first
      
    # 왼쪽 열을 위로 이동합니다.
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k + 1][y1]
        # 이동하는 동안의 최소값을 갱신합니다.
        min_value = min(min_value, matrix[k + 1][y1])
        
    # 아래쪽 행을 왼쪽으로 이동합니다.
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k + 1]
        # 이동하는 동안의 최소값을 갱신합니다.
        min_value = min(min_value, matrix[x2][k + 1])
        
    # 오른쪽 열을 아래로 이동합니다.
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k - 1][y2]
        # 이동하는 동안의 최소값을 갱신합니다.
        min_value = min(min_value, matrix[k - 1][y2])
        
    # 위쪽 행을 오른쪽으로 이동합니다.
    for k in range(y2, y1 + 1, -1):
        matrix[x1][k] = matrix[x1][k - 1]
        # 이동하는 동안의 최소값을 갱신합니다.
        min_value = min(min_value, matrix[x1][k - 1])
      
    # 회전의 시작 지점 바로 다음 위치에 최초의 값을 저장합니다.
    matrix[x1][y1 + 1] = first
    # 회전 과정에서 발견된 최소값을 반환합니다.
    return min_value

def solution(rows, columns, queries):
    # 주어진 행과 열에 따라 초기 행렬을 생성합니다.
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    # 결과값을 저장할 리스트입니다.
    result = []
    # 주어진 쿼리들을 순회하면서 rotate 함수를 호출합니다.
    for x1, y1, x2, y2 in queries:
        # rotate 함수의 결과(최소값)를 결과 리스트에 추가합니다.
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))
      
    # 모든 쿼리의 처리 결과인 최소값들의 리스트를 반환합니다.
    return result
