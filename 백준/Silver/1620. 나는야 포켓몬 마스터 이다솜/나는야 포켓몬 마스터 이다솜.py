# 정수 26, 5를 N, M으로 입력받기
import sys
N, M = map(int, sys.stdin.readline().split())

poketmon_name = dict()
poketmon_number= dict()

# 포켓몬 이름을 key로, 번호를 value로, 번호를 key로, 포켓몬 이름을 value로 하는 딕셔너리 생성
for i in range(1, N+1):
    poketmon = sys.stdin.readline().strip()
    poketmon_name[i] = poketmon
    poketmon_number[poketmon] = i

for i in range(M):
    find = sys.stdin.readline().strip()
    if find[0].isalpha():
        print(poketmon_number[find]) 
    else:
        print(poketmon_name[int(find)])