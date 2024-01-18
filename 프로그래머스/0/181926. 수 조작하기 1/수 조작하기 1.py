def solution(n, control):
    for target in control:
        if target == 'w':
            n += 1
        elif target == 's':
            n -= 1
        elif target == 'd':
            n += 10
        elif target == 'a':
            n -= 10
            
    return n