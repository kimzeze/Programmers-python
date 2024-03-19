# 재귀함수 최대치 상승 1000 -> 2000으로
import sys
sys.setrecursionlimit(2000) 

def solution(k, room_number): 
    rooms = dict()
    for num in room_number:
        chk_in = find_emptyroom(num,rooms)
    return list(rooms)

def find_emptyroom(chk, rooms):
    # 할당되지 않은 방이면?
    if chk not in rooms:
        # 방을 할당하면서 다음 방의 위치를 동시에 다시 저장
        rooms[chk] = chk + 1
        return chk
    empty = find_emptyroom(rooms[chk], rooms)
    # 찾은 방 + 1을 처음 방의 위치에서 
    rooms[chk] = empty + 1
    return empty