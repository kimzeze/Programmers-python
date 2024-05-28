def solution(data, ext, val_ext, sort_by):
    result = []
    answer = [[]]
    my_dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    # [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
    for target_data in data:
        if target_data[my_dict[ext]] < val_ext:
            result.append(target_data)
            
    result.sort(key = lambda x:x[my_dict[sort_by]])
            
    
    
    return result