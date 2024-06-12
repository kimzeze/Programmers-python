def solution(str1, str2):
    length = len(str2)
    count = len(str1) - len(str2) + 1
    for i in range(0, count):
        if str2 == str1[i:length+i]:
            return 1
    return 2