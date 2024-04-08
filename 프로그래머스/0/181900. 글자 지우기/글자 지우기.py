def solution(my_string, indices):

    string_arr = list(my_string)
    for target in indices:
        string_arr[target] = ''
    new_string = ''.join(string_arr)
        
    return new_string