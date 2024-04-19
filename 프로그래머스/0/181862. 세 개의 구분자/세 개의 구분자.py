def solution(myStr):
    answer = []
    replaceA = myStr.replace('a',' ')
    replaceB = replaceA.replace('b', ' ')
    result = replaceB.replace('c', ' ')
    answer = result.split()
    if answer == []:
        answer.append('EMPTY')
    return answer