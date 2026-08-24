def solution(prices):

n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        # 현재 가격보다 뒤에 있는 가격들을 하나씩 확인
        for j in range(i + 1, n):
            # 1초가 지났으므로 시간을 더함
            answer[i] += 1
            
            # 가격이 떨어졌다면? 더 이상 버티지 못하고 탈출!
            if prices[i] > prices[j]:
                break
                
    return answer