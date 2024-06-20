a, b = map(int, input().strip().split(' '))

answer = ''

for _ in range(b):
    answer += '*' * a
    answer += '\n'
    
print(answer)