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

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/e700fb330012e4efb04f99ec0b6c19a3
#
# [2026-03-30]
# ends = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
# --------------------------------------------------------------------------
