def solution(num):
    ans = 0
    # 조건 500번, 1이될떄까지
    while num != 1 and ans < 500:
        # num이 짝수인 경우
        if num % 2 == 0:
            num //= 2
        # num이 홀수인 경우
        else:
            num = num * 3 + 1
        ans += 1
    if ans == 500:
        return -1
    return ans