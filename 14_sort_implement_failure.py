def solution(N, stages):
    #1. stages[i]는 i번째 유저의 현재 위치를 의미함.
    #2. 스테이지 i의 실패율 = stages.count(i) / (스테이지 i 이상에 도달한 유저 수)

    reach_players = len(stages) # 도달한 유저수
    fail_rates=[]
    
    counts = [0 for _ in range(N)]
    
    for i in range(1, N + 1):
        current_players = stages.count(i)
        
        #0일때 예외처리
        if reach_players > 0:
            rate = current_players / reach_players
        else:
            rate = 0
            
        fail_rates.append((i, rate))
        reach_players -= current_players
        
    fail_rates.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    return [stage[0] for stage in fail_rates]