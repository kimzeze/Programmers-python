def solution(n):
    answer = 0
    my_list = []
    N = str(n)
    for i in N:
        my_list.append(i)
    my_list.sort(reverse=True)
    answer = "".join(my_list)
    return int(answer)