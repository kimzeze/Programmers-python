def solution(friends, gifts):
    # 1. 필요한 정보를 저장할 딕셔너리들을 만듭니다.
    gift_given = {friend: {} for friend in friends}  # 각 친구가 선물을 준 기록
    gift_received = {friend: {} for friend in friends}  # 각 친구가 선물을 받은 기록
    gift_score = {friend: 0 for friend in friends}  # 각 친구의 선물 지수
    next_month_gifts = {friend: 0 for friend in friends}  # 다음 달에 받을 선물의 수

    # 2. 선물 기록을 분석합니다.
    for gift in gifts:
        giver, receiver = gift.split()
        # 준 선물 기록
        if receiver in gift_given[giver]:
            gift_given[giver][receiver] += 1
        else:
            gift_given[giver][receiver] = 1
        # 받은 선물 기록
        if giver in gift_received[receiver]:
            gift_received[receiver][giver] += 1
        else:
            gift_received[receiver][giver] = 1
        # 선물 지수 계산
        gift_score[giver] += 1
        gift_score[receiver] -= 1

    # 3. 다음 달 선물 주고받기를 예측합니다.
    for i, friend1 in enumerate(friends):
        for friend2 in friends[i+1:]:
            # 두 친구가 서로 주고받은 선물의 수를 확인합니다.
            friend1_to_friend2 = gift_given[friend1].get(friend2, 0)
            friend2_to_friend1 = gift_given[friend2].get(friend1, 0)

            # 선물을 주고받은 기록이 있다면
            if friend1_to_friend2 != friend2_to_friend1:
                if friend1_to_friend2 > friend2_to_friend1:
                    next_month_gifts[friend1] += 1
                else:
                    next_month_gifts[friend2] += 1
            # 선물을 주고받은 기록이 없거나 같다면
            else:
                if gift_score[friend1] > gift_score[friend2]:
                    next_month_gifts[friend1] += 1
                elif gift_score[friend1] < gift_score[friend2]:
                    next_month_gifts[friend2] += 1
                # 선물 지수도 같다면 아무도 선물을 받지 않습니다.

    # 4. 가장 많은 선물을 받는 친구의 선물 수를 반환합니다.
    return max(next_month_gifts.values())
