def solution(a, b):
    strab = str(a) + str(b)
    int2ab = 2 * a * b
    int_strab = int(strab)
    if int_strab >= int2ab:
        return int_strab
    else:
        return int2ab
    
    