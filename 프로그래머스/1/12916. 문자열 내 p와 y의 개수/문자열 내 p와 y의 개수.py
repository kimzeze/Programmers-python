def solution(s):
    
    # 소문자로 변경
    target = s.lower()
    
    # p와 y의 개수 카운트    
    p = target.count('p')
    y = target.count('y')
    
    if p == y :
        return True
    else:
        return False