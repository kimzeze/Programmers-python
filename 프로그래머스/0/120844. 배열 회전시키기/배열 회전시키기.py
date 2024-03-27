def solution(numbers, direction):
    
    # 방향이 "left"일 경우
    if direction == "left":
        # 첫 번째 요소를 제거하고, 마지막에 추가
        first_element = numbers.pop(0)
        numbers.append(first_element)
        
    # 방향이 "right"일 경우
    elif direction == "right":
        # 마지막 요소를 제거하고, 처음에 추가
        last_element = numbers.pop()
        numbers.insert(0, last_element)
    
    # 수정된 배열 반환
    return numbers
