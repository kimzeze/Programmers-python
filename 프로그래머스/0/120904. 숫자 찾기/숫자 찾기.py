def solution(num, k):
    answer = 0
    for index, target in enumerate(str(num)):
        if target == str(k):
            return index + 1
    return -1