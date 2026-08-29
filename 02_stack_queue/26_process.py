from collections import deque

def solution(priorities, location):
    queues = deque((index,priority) for index, priority in enumerate(priorities))
    
    count = 0
    
    while queues:
        highest_priority = max(queues, key=lambda x: x[1])[1]
        current_index,current_priority = queues.popleft()
        
        if current_priority == highest_priority :
            count += 1
            if current_index == location :
                return count
        else :
            queues.append((current_index,current_priority))
            
            

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/11d1a2efd67184d431ca36d4ec73ed3d
#
# [2026-04-01]
# [opt] : deque 사용
# # list 대신 deque를 사용하면 popleft()가 O(1)로 처리됨
# # curr_idx, curr_p = queues.popleft() # pop(0) 대신 popleft()
#
#
# from collections import deque
#
# def solution(priorities, location):
#     # list 대신 deque를 사용하면 popleft()가 O(1)로 처리돼!
#     queues = deque((i, p) for i, p in enumerate(priorities))
#     count = 0
#
#     while queues:
#         # 현재 큐에서 가장 높은 우선순위 확인
#         max_p = max(queues, key=lambda x: x[1])[1]
#         curr_idx, curr_p = queues.popleft() # pop(0) 대신 popleft()
#
#         if curr_p == max_p:
#             count += 1
#             if curr_idx == location:
#                 return count
#         else:
#             queues.append((curr_idx, curr_p))
# --------------------------------------------------------------------------
