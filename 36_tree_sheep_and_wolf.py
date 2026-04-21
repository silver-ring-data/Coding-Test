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