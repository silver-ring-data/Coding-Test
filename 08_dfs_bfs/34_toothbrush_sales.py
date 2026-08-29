def solution(enroll, referral, seller, amount):
    # 1. 빠른 조회를 위해 {이름: 추천인} 딕셔너리 생성
    parent = dict(zip(enroll, referral))
    
    # 2. 각 판매원별 누적 수익을 저장할 딕셔너리 (초기값 0)
    total_profit = {name: 0 for name in enroll}
    
    # 3. 판매 기록을 하나씩 처리
    for s, a in zip(seller, amount):
        money = a * 100  # 칫솔 한 개당 100원
        
        curr_node = s
        while curr_node != "-" and money > 0:
            tax = money // 10  # 추천인에게 줄 10% (소수점 버림)
            my_profit = money - tax  # 내가 가질 금액
            
            # 내 수익 업데이트
            total_profit[curr_node] += my_profit
            
            # 추천인에게 올라갈 준비
            curr_node = parent[curr_node]
            money = tax
            
    # enroll 순서대로 결과 리스트 반환
    return [total_profit[name] for name in enroll]

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/ce4d8f3dc25b45ff987f1480590b2338
#
# [2026-04-19]
# opt
# [문제 핵심 요약]
# - 트리 구조: 판매원(노드)과 추천인(부모)의 관계를 파악해야 해.
# - 수익 배분: 판매 수익의 10%를 추천인에게 주고, 나머지는 본인이 가져.
#
# 중단 조건:
# - 추천인이 더 이상 없을 때 (중앙 센터 -에 도달).
# - 배분할 금액(10%)이 1원 미만(0원)일 때 (이걸 놓치면 시간 초과가 날 수 있어).
# --------------------------------------------------------------------------
