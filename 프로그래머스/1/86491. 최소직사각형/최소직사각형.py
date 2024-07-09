def solution(sizes):
    answer = 0
    max_size = []
    min_size = []
    
    
    for size in sizes:
        max_size.append((max(size)))
        min_size.append((min(size)))
    
    answer = max(max_size) * max(min_size)
    
    return answer