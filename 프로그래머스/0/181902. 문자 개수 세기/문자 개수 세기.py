def solution(my_string):
    answer = [0] * 52
    # A = 65, Z = 90, a = 97, z = 122
    
    for string in my_string:
        if ord(string) >= 65 and ord(string) <= 90:
            answer[ord(string)-65] += 1
        elif ord(string) >= 97 and ord(string) <= 122:
            answer[ord(string)-71] += 1
        
    return answer