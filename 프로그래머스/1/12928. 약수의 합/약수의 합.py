def solution(n):
    answer = 0
    my_list = []
    
    # 약수 구하기
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            my_list.append(i)
    my_list.append(n)
    print(my_list)
    answer = sum(my_list)
    return answer