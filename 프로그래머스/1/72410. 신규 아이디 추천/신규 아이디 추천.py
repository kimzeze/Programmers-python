# 정규식
import re

def solution(new_id):
    answer = ''
    # 1단계: 대문자 -> 소문자 변환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = re.sub('\.+', '.', new_id)
    
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = re.sub('^\.|\.$', '', new_id)
    
    # 5단계: 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == '':
        new_id = 'a'
    
    # 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자 제거 및 마지막 마침표(.)를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id