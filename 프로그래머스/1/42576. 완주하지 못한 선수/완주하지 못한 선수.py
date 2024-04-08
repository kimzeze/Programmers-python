def solution(participant, completion):
    # participant와 completion 리스트를 정렬합니다.
    participant.sort()
    completion.sort()
    
    # completion 리스트의 길이만큼 반복하여,
    # participant와 completion을 비교하여 완주하지 못한 참가자를 찾습니다.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 만약 위 반복문에서 완주하지 못한 참가자가 발견되지 않으면,
    # participant 리스트의 마지막 요소가 완주하지 못한 참가자입니다.
    return participant[-1]

# 테스트를 위한 예시 입력
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))  # 출력: "leo"
