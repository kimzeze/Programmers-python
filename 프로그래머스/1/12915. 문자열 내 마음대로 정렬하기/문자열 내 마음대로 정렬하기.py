def solution(strings, n):
    # 주어진 리스트를 가공하여 (n번째 이전 문자열, n번째 문자열)의 형태로 저장
    processed_strings = []
    for string in strings:
        processed_strings.append((string[n], string))
    
    # 가공한 문자열을 기준으로 정렬
    processed_strings.sort()
    
    # 정렬된 결과에서 두 번째 인덱스 값을 반환
    sorted_strings = []
    for processed_string in processed_strings:
        sorted_strings.append(processed_string[1])
    
    return sorted_strings