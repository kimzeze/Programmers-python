def solution(a, b):
    # a,b 홀수
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    # a와 b 중 하나만 홀수인 경우
    elif (a % 2 == 1 and b % 2 == 0) or (a % 2 == 0 and b % 2 == 1):
        return 2 * (a + b)
    else:
        return abs(a-b)
