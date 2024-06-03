def solution(cipher, code):
    answer = ''
    
    length = len(cipher) // code
    
    for i in range(1, length+1):
        answer += (cipher[i*code-1])
        
    return answer