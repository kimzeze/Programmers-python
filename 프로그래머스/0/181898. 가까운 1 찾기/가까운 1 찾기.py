def solution(arr, idx):
    if arr[idx] == 1:
        return idx
    for i in range(idx + 1, len(arr)):
        if arr[i] == 1:
            return i
    return -1