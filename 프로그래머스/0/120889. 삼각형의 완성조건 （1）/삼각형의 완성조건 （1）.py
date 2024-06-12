def solution(sides):
    # 리스트를 내림차순으로 정렬
    sides.sort(reverse=True)
    
    if sides[0] < sides[1] + sides[2]:
        return 1
    else:
        return 2