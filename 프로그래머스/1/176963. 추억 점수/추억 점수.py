def solution(name, yearning, photo):
    answer = []
    dictionary = {}
    
    # 딕셔너리에 {이름 : 점수}로 만들어주기
    for i in range(len(name)):
        dictionary[name[i]] = yearning[i]
        
    print(dictionary)
    
    # photo 이중 배열 순회 [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
    for target in photo:
        
        # 배열 돌때마다 스코어 초기화
        score = 0
        print('스코어 초기화', score)
        
        # 첫번째 배열 -> ["may", "kein", "kain", "radi"]
        for person in target: 
            # "may"
            if person in dictionary: 
                person_score = dictionary[person] # dictionary['may'] -> 5
                score += person_score
                print('current score', score)
        answer.append(score)
    return answer