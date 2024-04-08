def solution(myString, pat):
    index = myString.rindex(pat)
    print(index)
    answer = myString[:index + len(pat)]
    return answer