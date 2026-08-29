# 38_col_ponkemon.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/7e5807de169bbadfc0bc81dd178bf4ec

## 2026-04-24

[opt]
```
def solution(nums):
    pick_limit = len(nums) // 2
    unique_types_count = len(set(nums))
    
    # 두 값 중 최솟값 선택
    # 이유: if-else 문보다 min()을 쓰면 "제한 사항 내에서 최선을 선택한다"는 의도가 명확해져.
    return min(pick_limit, unique_types_count)
```
