def solution(myString):
    answer = []
    stringA = myString.split('x')
    stringB = ' '.join(stringA).split()
    
    return sorted(stringB)