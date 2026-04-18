from collections import deque

def solution(maps):
    
    start_pos = find_location(maps, "S")
    lever_pos = find_location(maps, "L")
    
    # 시작점 -> 레버
    dist_to_lever = move(start_pos, "L", maps)
    
    if dist_to_lever == -1:
        return -1
    
    # 3. 레버 -> 출구
    dist_to_exit = move(lever_pos, "E", maps)
    
    if dist_to_exit == -1:
        return -1
        
    return dist_to_lever + dist_to_exit

def find_location(maps, target): # S, L, E 찾기
    for y, row in enumerate(maps): 
        for x, char in enumerate(row): 
            if char == target:
                return y,x
            
def move(current_pos, target_char, maps):
    rows = len(maps)
    cols = len(maps[0])

    cur_y, cur_x = current_pos
    queue = deque([(cur_y, cur_x, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[cur_y][cur_x] = True
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:
        y, x, dist = queue.popleft()
        
        # 목표 지점에 도착
        if maps[y][x] == target_char:
            return dist
            
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            # 벽이나 유효한 위치에 잇는지 확인
            if not (0 <= ny < rows and 0 <= nx < cols):
                continue
            if maps[ny][nx] == 'X' or visited[ny][nx]:
                continue
                
            # 방문 처리 후 큐에 삽입
            visited[ny][nx] = True
            queue.append((ny, nx, dist + 1))
            
    # 큐가 빌 때까지 못 찾았다면 도달 불가능
    return -1
        