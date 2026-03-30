def solution(progresses, speeds):
    ends = []
    for prog, speed in zip(progresses, speeds) :
        end = (100 - prog)//speed
        end_remain = (100 - prog)%speed
        if end_remain :
            end += 1
        ends.append(end)
    
    answer = []
    current_day = ends[0]
    count = 1 
    for i in range(1, len(ends)):
        if ends[i] <= current_day:
            count += 1
        else:
            answer.append(count)
            current_day = ends[i]
            count = 1
    answer.append(count)
    return answer