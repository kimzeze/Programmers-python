def solution(s):
    answer = ''
    length = len(s)
    if length % 2 == 0 :
        answer += s[length // 2 - 1]
        answer += s[length // 2]
    else:
        answer += s[(length + 1) // 2 -1]
    return answer