def solution(s):
    ans = 0
    # 문자열 인덱스
    index = 0  
    # 문자열의 길이
    length = len(s)

    while index < length:
        # 현재 인덱스의 문자를 x로 설정
        x = s[index]
        
        # x의 개수와 x가 아닌 문자의 개수
        x_count = 0
        not_x_count = 0
        
        for i in range(index, length):
            # 현재 문자가 x인 경우 x_count 증가
            if s[i] == x:
                x_count += 1
            # 현재 문자가 x가 아닌 경우 not_x_count 증가
            else:
                not_x_count += 1
            
            # x의 개수와 x가 아닌 문자의 개수가 같아지면
            if x_count == not_x_count:
                # 분해된 문자열의 개수 증가
                ans += 1
                # 다음 인덱스로 이동
                index = i + 1
                # 반복문 종료
                break
        
        # 끝까지 개수가 다른 경우
        if x_count != not_x_count:
            # 분해된 문자열의 개수 증가
            ans += 1
            break
    
    return ans