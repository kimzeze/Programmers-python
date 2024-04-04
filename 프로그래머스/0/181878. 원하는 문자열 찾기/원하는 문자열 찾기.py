def solution(myString, pat):
    lowString = myString.lower()
    lowPat = pat.lower()
    if lowPat in lowString:
        return 1
    else:
        return 0