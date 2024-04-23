def solution(s):
    answer = []
    dictionary = {}
    
    for i, string in enumerate(s):
        # 딕셔너리에 초기값들 넣기
        if string not in dictionary:
            dictionary[string] = [i]
            # -1 넣어줌
            answer.append(-1) 
        # 딕셔너리에 중복된 값이 있으면?
        else:
            # 거리 계산
            distance = i - dictionary[string][-1]
            answer.append(distance)
            dictionary[string].append(i)
    
    print(dictionary)
    print(answer)

    return answer
