def solution(board, h, w):
    #[
    #["blue", "red", "orange", "red"], 
    #["red", "red", "blue", "orange"], 
    #["blue", "orange", "red", "red"], 
    #["orange", "orange", "red", "blue"]
    #]
    
    answer = 0
    
    # board의 길이
    n = len(board)
    
    # 같은 색칠 칸 개수
    count = 0
    
    # h와 w의 변화량을 저장할 정수 리스트
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    for i in range(4):
        h_check = h+dh[i]
        w_check = w+dw[i]
        
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n :
            if board[h][w] == board[h_check][w_check]:
                count += 1
                
    return count