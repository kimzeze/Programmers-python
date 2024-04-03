def solution(myString):
    # x 기준으로 문자열 나누기
    substrings = myString.split('x')
    lengths = []
    for substring in substrings:
        lengths.append(len(substring))
    return lengths