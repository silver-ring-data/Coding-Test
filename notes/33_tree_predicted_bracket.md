# 33_tree_predicted_bracket.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/21d5a4a4485214d42b0e381f55a7cf2d

## 2026-04-15

[opt] 
내가 짠 코드는 현재를 기준으로 판단하지만,
재미나이는 미래 단계를 기점으로 판단.
```
def solution(n, a, b):
    answer = 0
    
    # 두 참가자가 만날 때까지 반복
    while a != b:
        a = get_next_number(a)
        b = get_next_number(b)
        answer += 1
        
    return answer

def get_next_number(current_number):
    """
    다음 라운드 번호를 계산하는 헬퍼 함수
    이유: (n + 1) // 2 식의 의도를 명확히 전달하기 위함
    """
    return (current_number + 1) // 2
```
