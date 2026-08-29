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
        

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/da97a55be6f0f40acdf761a5babac571
#
# [2026-04-18]
# init : 왔던 곳을 체크하는 걸 어떻게 해야할지 모르겠음
#
# [2026-04-20]
# 인덱스 접근엔 list,
# 앞부분 추가/삭제는 deque가 유리
#
# [2026-04-20]
# (0,0) S  O  O
# (1,0) O  X  O  (X는 벽)
# (2,0) O  O  L
#
# 이라고 가정할 때, 흐름은 아래와 같음
# -0단계: 시작점 세팅 (거리 0)
# Queue: [(0,0,0)] (S점, 거리 0 적힌 쪽지 1번)
# Visited: (0,0)에 도장 쾅!
#
# -1단계: 거리 1인 곳들 방문
# 큐에서 (0,0,0) 꺼냄. (S점 확인)
# S 주변(상하좌우) 탐색: (0,1)과 (1,0) 발견! 벽(X) 아님, 방문 안 함.
# Queue: [(0,1,1), (1,0,1)] (새로 발견한 곳들, 거리 1 쪽지 추가)
# Visited: (0,1), (1,0)에 도장 쾅!
#
# -2단계: 거리 2인 곳들 방문
# 큐에서 (0,1,1) 꺼냄. (동쪽 O 확인)
# 주변 탐색: (0,2) 발견!
# Queue: [(1,0,1), (0,2,2)] (거리 2 쪽지 추가)
# Visited: (0,2)에 도장 쾅!
# 큐에서 (1,0,1) 꺼냄. (남쪽 O 확인)
# 주변 탐색: (2,0) 발견! (1,1은 벽이라 패스)
# Queue: [(0,2,2), (2,0,2)] (거리 2 쪽지 추가)
# Visited: (2,0)에 도장 쾅!
#
# -3단계: 거리 3인 곳들 방문
# 큐에서 (0,2,2) 꺼냄. (동쪽 끝 O 확인)
# 주변 탐색: (1,2) 발견!
# Queue: [(2,0,2), (1,2,3)] (거리 3 쪽지 추가)
# Visited: (1,2)에 도장 쾅!
# 큐에서 (2,0,2) 꺼냄. (남쪽 끝 O 확인)
# 주변 탐색: (2,1) 발견!
# Queue: [(1,2,3), (2,1,3)] (거리 3 쪽지 추가)
# Visited: (2,1)에 도장 쾅!
#
# -4단계: 거리 4인 곳들 방문
# 큐에서 (1,2,3) 꺼냄. (O 확인)
# 주변 탐색: (2,2) 발견! 앗, 여기가 우리가 찾던 **L(레버)**이네! ✨
# 즉시 종료: 현재 거리 3에 +1을 한 **4**를 반환! 🏁
# --------------------------------------------------------------------------
