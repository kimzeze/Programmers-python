def solution(survey, choices):
    answer = ''
    # 설문조사 길이
    length = len(survey)
    
    # 성격 유형 
    personality = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0 }
    
    # 각 성격유형 별로 점수 계산
    for i in range(length):
        if choices[i] > 4 :
            target = survey[i][1]
            personality[target] += choices[i] - 4
        elif choices[i] < 4:
            target = survey[i][0]
            personality[target] += 4 - choices[i]

    # 여기서부터 추가된 코드
    type_pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for a, b in type_pairs:
        if personality[a] >= personality[b]:
            answer += a
        else:
            answer += b
    
    return answer