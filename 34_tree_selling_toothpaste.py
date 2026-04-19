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