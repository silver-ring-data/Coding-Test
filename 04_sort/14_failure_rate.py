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

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/30b65559e636a44789bd1c9f6b8113c8
#
# [2026-03-16]
# [fix] : "만약 실패율이 같은 스테이지가 있다면 번호가 작은 스테이지가 먼저 와야 한다." 의 조건 처리 필요
#
# [2026-03-16]
# * 시간이 좀 없어서 이번꺼는 많이 하지 못함 ㅜㅜ
# --------------------------------------------------------------------------
