from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        current_course_combi = []
        for order in orders:
            # ['X', 'Y', 'Z'] -> (2) -> ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')
            current_course_combi += combinations(sorted(order), c)
            
        if current_course_combi: # 조합이 하나도 없는경우 체크
            counts = Counter(current_course_combi) # 횟수 카운트
            max_val = max(counts.values()) # 가장 많이 주문된 횟수

            if max_val >= 2: # 최소 2명 이상 주문 조건
                for key, value in counts.items():
                    if value == max_val: # 가장 많이 시켰을 경우
                        # 튜플을 문자열로 바꿔서 answer에 추가
                        answer.append("".join(key))
    return sorted(set(answer))