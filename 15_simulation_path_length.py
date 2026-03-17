
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
