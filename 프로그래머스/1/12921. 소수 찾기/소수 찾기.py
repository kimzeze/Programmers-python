def solution(n):
    # 소수의 개수를 셀 변수 count를 0으로 초기화합니다.
    count = 0
    
    # 2부터 n까지의 숫자를 하나씩 검사합니다.
    for num in range(2, n + 1):
        # 각 숫자가 소수인지 확인하기 위한 변수 is_prime을 True로 초기화합니다.
        is_prime = True
        
        # 2부터 num의 제곱근까지의 숫자로 num을 나누어봅니다.
        # 제곱근까지만 검사하는 이유는 효율성을 위해서입니다.
        for i in range(2, int(num ** 0.5) + 1):
            # 만약 num이 i로 나누어떨어진다면, 소수가 아닙니다.
            if num % i == 0:
                is_prime = False
                break  # 소수가 아님이 확인되었으므로 더 이상 검사할 필요가 없습니다.
        
        # num이 소수라면 count를 1 증가시킵니다.
        if is_prime:
            count += 1
    
    # 소수의 개수 count를 반환합니다.
    return count