def solution(picture, k):
    answer = []
    row_picture = len(picture)
    col_picture = len(picture[0])

    for i in range(row_picture):
        row = picture[i]
        for _ in range(k):
            expanded_row = ''
            for j in range(col_picture):
                expanded_row += row[j] * k
            answer.append(expanded_row)

    return answer