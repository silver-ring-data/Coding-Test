# 31_hash_menu_renew.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/590bbb33313dbe3a61afabd88be5461c

## 2026-04-13

from itertools import combinations
from collections import Counter

## 2026-04-13

opt
```
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for size in course:
        # 1. 모든 주문에서 해당 크기의 조합을 한 번에 추출 (Better Way 7: 리스트 컴프리헨션 활용)
        order_combinations = []
        for order in orders:
            order_combinations.extend(combinations(sorted(order), size))
        
        # 2. 조합이 없으면 다음 크기로 넘어감 (방어적 코딩)
        if not order_combinations:
            continue
            
        # 3. 빈도수 계산
        counts = Counter(order_combinations)
        if not counts:
            continue
            
        # 4. 가장 많이 주문된 횟수 찾기
        max_val = max(counts.values())
        
        # 5. 조건에 맞는 메뉴 추출 (최소 2명 이상, 최대 빈도와 일치)
        if max_val >= 2:
            # Better Way 29: 대입 식(Walrus operator)을 쓰거나 가독성을 위해 필터링
            for menu, count in counts.items():
                if count == max_val:
                    answer.append("".join(menu))
                    
    return sorted(answer)
```
