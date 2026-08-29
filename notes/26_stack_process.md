# 26_stack_process.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/11d1a2efd67184d431ca36d4ec73ed3d

## 2026-04-01

[opt] : deque 사용
# list 대신 deque를 사용하면 popleft()가 O(1)로 처리됨
# curr_idx, curr_p = queues.popleft() # pop(0) 대신 popleft()


from collections import deque

def solution(priorities, location):
    # list 대신 deque를 사용하면 popleft()가 O(1)로 처리돼!
    queues = deque((i, p) for i, p in enumerate(priorities))
    count = 0
    
    while queues:
        # 현재 큐에서 가장 높은 우선순위 확인
        max_p = max(queues, key=lambda x: x[1])[1]
        curr_idx, curr_p = queues.popleft() # pop(0) 대신 popleft()
        
        if curr_p == max_p:
            count += 1
            if curr_idx == location:
                return count
        else:
            queues.append((curr_idx, curr_p))
