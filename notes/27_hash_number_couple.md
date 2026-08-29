# 27_hash_number_couple.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/3ec7d26f095028bd6d454160618a2e15

## 2026-04-02

[opt]
1. Counter 사용 # {'숫자':해당 숫자의 카운팅}
2. range(9, -1, -1)으로 reverse를 미리

```from collections import Counter

def solution(X, Y):
    # 1. 각 숫자의 빈도수를 미리 계산 (성능 최적화)
    x_count = Counter(X)
    y_count = Counter(Y)
    
    answer_list = []
    
    # 2. 9부터 0까지 역순으로 확인하여 정렬 비용 제거 (Clean Code: 명확한 의도)
    for i in range(9, -1, -1):
        char_num = str(i)
        # 공통으로 나타나는 횟수만큼 추가
        count = min(x_count[char_num], y_count[char_num])
        answer_list.append(char_num * count)
    
    # 3. 예외 처리: 가드 클로즈(Guard Clauses) 패턴
    joined_answer = "".join(answer_list)
    
    if not joined_answer:
        return "-1"
    
    # 가장 큰 숫자가 '0'이면 나머지도 다 '0'임 (내림차순 정렬의 이점)
    if joined_answer[0] == "0":
        return "0"
        
    return joined_answer```
