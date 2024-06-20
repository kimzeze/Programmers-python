def solution(s):
    length = len(s)
    
    
    
    if (length == 4 or length == 6) and s.isdigit():
        return True
    else:
        return False
        