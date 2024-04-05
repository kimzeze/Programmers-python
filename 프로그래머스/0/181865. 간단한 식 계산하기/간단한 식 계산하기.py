def solution(binomial):
    answer = ''
    arr = binomial.split(' ')
    if '+' in arr:
        answer = int(arr[0]) + int(arr[2])
    if '-' in arr:
        answer = int(arr[0]) - int(arr[2])
    if '*' in arr:
        answer = int(arr[0]) * int(arr[2])
    return answer