def solution(citations):
    # 1. 논문 배열을 받아서 (인용 횟수 모음 배열, ex. [3,0,6,1,5])
    # 2. 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # 3.
    for index, citation in enumerate(citations):
        if index >= citation:
            return index
        
    return len(citations)