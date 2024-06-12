def solution(n):
    target = n**(1/2)
    if target == int(target):
        return 1
    else:
        return 2