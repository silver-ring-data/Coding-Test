
def solution(dirs):
    move_dir ={
        'U' : (0, 1),
        'D' : (0, -1),
        'R' : (1, 0),
        'L' : (-1, 0)
    }
    
    current_x = 0
    current_y = 0
    unique_paths = set()
    paths = [(current_x, current_y)]
    
    # 경로 저장
    for dir in dirs :
        move_x, move_y = move_dir[dir]
        next_x, next_y = current_x + move_x, current_y + move_y
        
        if abs(next_x) > 5 or abs(next_y) > 5:
           continue
        
        unique_path = tuple(sorted([(current_x, current_y), (next_x, next_y)]))
        unique_paths.add(unique_path)
        
        current_x, current_y = next_x, next_y
        
    return len(unique_paths)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/fc03c6c33cbd2362441512cb3409c1e4
#
# [2026-03-17]
# [init] : 일반 중복제거 없이 처음에 짠 알고리즘 -> 중복제거 추가하고 (현재 좌표, 이동좌표) 로 묶어서 중복제거를 해야함
#
# [2026-03-17]
# [fix] : 오타 수정 enumerate 안쓰는데 쓴거 지우기
# ++ -> +=
# -- -> -= 로 바꾸기
#
# [2026-03-18]
# [opt] : dir을 딕셔너리 형태로 저장해서 반복적인 코드 제거
# --------------------------------------------------------------------------
