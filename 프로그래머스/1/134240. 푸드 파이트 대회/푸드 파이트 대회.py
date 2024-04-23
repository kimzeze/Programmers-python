def solution(food):
    answer = ''
    dictionary = {}
    for index, amount in enumerate(food):
        if amount // 2 != 0:
            dictionary[index] = amount // 2
    
    for key, value in dictionary.items():
        answer += str(key) * value
        
    reverse = answer[::-1]
    answer = answer + '0' + reverse

    print(reverse)
    return answer