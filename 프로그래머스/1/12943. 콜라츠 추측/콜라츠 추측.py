def collatz(num, ans):
    # 입력 숫자가 1이면 ans를 반환하고 종료
    if num == 1:
        return ans
    # 만약 500번 이상될 때 까지 반복한다면 -1을 반환하고 종료
    if ans == 500:
        return -1
    
    # 짝수일 경우
    if num % 2 == 0:
        return collatz(num // 2, ans + 1)
    # 홀수일 경우
    elif num % 2 == 1:
        return collatz(num * 3 + 1, ans + 1)

def solution(num):
    return collatz(num, 0)

