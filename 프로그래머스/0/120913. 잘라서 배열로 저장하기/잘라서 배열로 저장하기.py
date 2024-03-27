def solution(my_str, n):
    result = []
    
    # 문자열의 길이만큼 반복하면서 n 길이만큼 잘라서 결과 배열에 추가
    for i in range(0, len(my_str), n):
        # 문자열을 n 길이만큼 잘라서 result 배열에 추가
        result.append(my_str[i:i+n])
    
    # 결과 배열 반환
    return result