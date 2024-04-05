def solution(myString, pat):
    answer = ''
    for str1 in myString:
        if "A" in str1:
            answer += 'B'
        elif "B" in str1:
            answer += 'A'
    if pat in answer:
        return 1
    else:
        return 0