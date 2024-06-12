def solution(dot):
    
    answer = 0
    
    # 1사분면
    if dot[0] > 0 and dot[1] > 0:
        return 1
    # 2사분면
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    # 3사분면
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4
    