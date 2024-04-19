def solution(arr):
    length = len(arr)
    answer = []
    zero = 0
    double_list = [1,2,4,8,16,32,64,128,256,512,1024]
    for i in range(len(double_list)):
        if length <= double_list[i]:
            zero = double_list[i] - length
            break
    for j in range(zero):
        arr.append(0)
    return arr