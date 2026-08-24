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
            
            