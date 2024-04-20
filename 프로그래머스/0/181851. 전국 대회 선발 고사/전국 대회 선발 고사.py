def solution(rank, attendance):
    group = {}
    length = len(rank)
    
    for index, student in enumerate(rank):
        group[index] = [student]
        
        
    for i in range(len(attendance)):
        if attendance[i] == False:
            del group[i]
    
    sorted_group = sorted(group.items(), key=lambda x: x[1])

    a, b, c = sorted_group[0][0], sorted_group[1][0], sorted_group[2][0]

    return 10000 * a + 100 * b + c