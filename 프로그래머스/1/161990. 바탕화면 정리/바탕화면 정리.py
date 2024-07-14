def solution(wallpaper):
    answer = []
    length = len(wallpaper)
    # 시작 세로, 가로
    start_col = []
    start_row = []
    # 마지막 세로
    finish_col = []
    finish_row = []
    
    for i in range(length):
        reverse = wallpaper[i][::-1]
        if '#' in wallpaper[i]:
            start_col.append(i)
            start_row.append(wallpaper[i].index('#'))
            finish_row.append(i + 1)
            finish_col.append(len(reverse) - reverse.index('#'))
    
    answer.append(min(start_col))
    answer.append(min(start_row))
    answer.append(max(finish_row))
    answer.append(max(finish_col))
        
    return answer