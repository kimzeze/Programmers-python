def solution(myString):
    answer = ''
    for string in myString:
        if string < 'l':
            answer += 'l'
        else :
            answer += string
    return answer