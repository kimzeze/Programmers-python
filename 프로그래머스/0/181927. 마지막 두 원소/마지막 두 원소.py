def solution(num_list):
    targetA = num_list[-1]
    targetB = num_list[-2]
    if targetA > targetB:
        num_list.append(targetA-targetB)
    else:
        num_list.append(targetA*2)
    
    return num_list