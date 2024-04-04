def solution(numbers):
    # answer는 중복된 원소합의 배열 
    answer = []
    # REAL_ANSWER는 중복된 원소합의 배열
    REAL_ANSWER = []
    # 배열 길이
    length = len(numbers)
    
    # 모든 수를 다 더해서 answer에 넣음
    for i in range(length):
        for j in range(length):
            # 똑같은 인덱스는 넣지 않음
            if i != j:
                answer.append(numbers[i]+numbers[j])  
                
    # REAL_ANSWER에 없는 원소만 answer에서 가져다 넣음
    for ans in answer:
        if ans not in REAL_ANSWER:
            REAL_ANSWER.append(ans)
        
    # 오름차순으로 정렬
    return sorted(REAL_ANSWER)