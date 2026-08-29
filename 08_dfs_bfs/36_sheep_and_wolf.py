def solution(info, edges):
    # 1. 트리 구성 (인접 리스트)
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)
    
    answer = []

    # 2. 핵심 탐색 함수
    def find_sheep(current_node, sheep, wolf, next_candidates):
        # [업데이트] 현재 노드의 양/늑대 정보를 확인해서 카운트 반영
        if info[current_node] == 0:
            sheep += 1
        else:
            wolf += 1
            
        # [조건 확인] 만약 늑대 수 >= 양의 수라면 탐색 종료
        if wolf >= sheep:
            return
            
        # [결과 기록] 현재까지 모은 양의 수를 기록
        answer.append(sheep)
        
        # [후보지 업데이트] 
        # 현재 노드에서 갈 수 있는 자식들을 추가하고, 현재 노드는 후보에서 제외
        new_candidates = [n for n in next_candidates if n != current_node]
        new_candidates.extend(tree[current_node])
        
        # [재귀 호출] 새로운 후보지에 있는 노드들을 하나씩 방문
        for next_node in new_candidates:
            find_sheep(next_node, sheep, wolf, new_candidates)

    # 0번 노드(루트)부터 시작! 초기 후보지에 0번을 넣어줘.
    find_sheep(0, 0, 0, [0])
    
    return max(answer)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/bfbf06ca29040ef5d5a664b4de835044
#
# [2026-04-21]
# [코드 실행 흐름 시뮬레이션]
#
# 1. 시작 (루트 노드 방문)
#
# find_sheep(0, 0, 0, [0]) 호출
# info[0]은 양이니까 sheep은 1이 돼.
# answer에 [1]이 저장되고, 0번의 자식인 [1, 2]를 후보에 넣어.
# 새로운 후보: [1, 2] (0은 빠지고 자식들이 추가됨)
#
# 2. 2번 노드(양)로 먼저 가보기
#
# 루프를 돌다가 find_sheep(2, 1, 0, [1, 2]) 호출
# info[2]는 양이니까 sheep은 2가 돼.
# answer에 [1, 2]가 저장돼.
# 2번의 자식은 없으니까 후보에서 2만 빠져.
# 새로운 후보: [1]
#
# 3. 1번 노드(늑대)로 가보기 (점프!)
#
# 이제 후보에 남은 1을 방문해: find_sheep(1, 2, 0, [1]) 호출
# info[1]은 늑대니까 wolf는 1이 돼.
# wolf(1) < sheep(2)니까 통과! answer에 [1, 2, 2]가 저장돼.
# 새로운 후보: [] (더 갈 곳이 없으니 이쪽 길 탐색 종료)
# --------------------------------------------------------------------------
