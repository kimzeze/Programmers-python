def solution(bandage, health, attacks):
    t, x, y = bandage  # 붕대 감기 시간, 초당 회복량, 추가 회복량
    max_health = health  # 최대 체력 저장
    last_attack_time = attacks[-1][0]  # 마지막 공격 시간
    attack_dict = dict(attacks)  # 공격 시간과 데미지를 딕셔너리로 변환

    consecutive_heal = 0  # 연속 붕대 감기 시간
    
    for current_time in range(1, last_attack_time + 1):
        if current_time in attack_dict:
            # 공격 받은 경우
            health -= attack_dict[current_time]
            consecutive_heal = 0
            if health <= 0:
                return -1  # 캐릭터 사망
        else:
            # 붕대 감기
            health += x
            consecutive_heal += 1
            
            if consecutive_heal == t:
                # 붕대 감기 완료
                health += y
                consecutive_heal = 0
            
            health = min(health, max_health)  # 최대 체력 초과 방지
    
    return health