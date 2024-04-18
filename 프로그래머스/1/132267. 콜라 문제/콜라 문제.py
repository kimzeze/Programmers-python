def solution(a, b, n):
    result = 0

    while n >= a:
        cola = (n // a) * b
        result += cola
        n = (n % a) + cola

    return result