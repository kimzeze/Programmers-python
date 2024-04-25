def solution(nums):
    count = {}
    
    for monster in nums:
        # 해당 포켓몬이 딕셔너리에 없으면 키 = 이름, 값 = 1 추가
        if monster not in count:
            count[monster] = 1
            
        # 있는 경우 값을 1 증가
        else:
            count[monster] += 1
            
    print(count)
    
    # 선택할 포켓몬 종류의 수 (N/2개)
    choice_monster = len(nums) // 2
    
    count_monster = len(count)

    
    # 선택한 포켓몬 종류의 수와 선택 가능한 포켓몬 종류의 수를 비교하여 더 작은 값을 반환
    return min(choice_monster, count_monster)

