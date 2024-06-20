def solution(s):
    answer = ''
    word_index = 0
    
    for char in s:
        if char == ' ':
            answer += char
            word_index = 0  # 단어 구분 후 인덱스 초기화
        else:
            if word_index % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
            word_index += 1
    
    return answer
