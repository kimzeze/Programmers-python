def solution(hp):
    answer = 0
    jang = hp // 5
    beung = (hp % 5) // 3
    ill = (hp % 5) % 3
    
    answer = jang + beung + ill
    
    return answer