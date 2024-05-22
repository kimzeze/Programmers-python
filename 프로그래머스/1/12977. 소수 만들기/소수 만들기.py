from itertools import combinations

def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        
        # 조합의 합
        getSum = sum(i)
        
        for j in range(2, int(getSum ** 0.5) + 1):
            if getSum % j == 0:
                break
        else:
            answer += 1  # 소수인 경우에만 증가

    return answer