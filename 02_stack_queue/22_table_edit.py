def solution(n, k, cmd):
    results = ['O'] * n
    deletes = [] # (이전행, 현재행, 다음행)의 튜플 리스트임
    # n = 처음 표의 행 개수
    # k = 현재 위치
    table = {i: [i - 1, i + 1] for i in range(n)} # {현재행: [이전행, 다음행]}
    
    table[0][0] = None
    table[n - 1][1] = None
    
    for index, command in enumerate(cmd) :
        if len(command) >= 2 : 
            direction, count = command.split()
            count = int(count)
            if direction == 'U' :
                for _ in range(count) :
                    k = table[k][0] # 이전행으로 한칸 이동
            else :
                for _ in range(count) :
                    k = table[k][1] # 다음행으로 한칸 이동
        else :
            if command == 'C' :
                prev, next = table[k] # 이전행/다음행
                
                deletes.append((prev, k, next)) # deletes에 삭제 데이터 넣기
                results[k] = 'X' # result에 반영
                
                if prev is not None: # 삭제한 후 이전행이 처음이 아니라면 
                    table[prev][1] = next # 이전행의 다음은 현재행이 아니라 다음행임
                if next is not None: # 삭제한 후 다음행이 마지막이 아니라면 
                    table[next][0] = prev # 다음행의 이전은 현재행이 아니라 이전행임
                
                if next is not None : # 삭제한 행의 다음이 존재한다면
                    k = next # 현재행을 다음행으로 변경
                else : # 삭제한 행이 끝에 있다면
                    k = prev  # 현재행을 이전행으로 변경
                
            else : #Z
                prev, restored, next = deletes.pop() #deletes에서 꺼내오기
                results[restored] = 'O' # 복구한 행의 result 상태 변경
                
                if prev is not None: # 이전 행이 처음이 아닌경우 
                    table[prev][1] = restored # 이전행의 다음행은 다음행이 아니라 현재행
                if next is not None: # 다음 행이 마지막 아닌경우
                    table[next][0] = restored # 다음행의 이전행은 이전행이 아니라 현재행
        
    return "".join(results)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/9bbd8172480bb618f1d3cf9c06bfa373
#
# [2026-03-26]
# init : 일단 로직 반영을 다 못함
# - 삭제된 행 번호도 저장해야되는데, 이럴거면 그냥 초기 리스트를 딕셔너리로 소환해서 관리하는게 나을거같음
#
# [2026-03-26]
# [refactor] table = {i: [i - 1, i + 1] for i in range(n)} # {현재행: [이전행, 다음행]} 이렇게 바꾼게 주요하였음.
#
# [2026-03-26]
# [opt]: # c.startswith : 특정 문자가 있는지 확인하는 매서드라고 함
#
# def solution(n, k, cmd):
#     # 1. 연결 리스트 초기화 {현재: [이전, 다음]}
#     table = {i: [i - 1, i + 1] for i in range(n)}
#     table[0][0] = None
#     table[n - 1][1] = None
#
#     results = ['O'] * n
#     deletes = [] # 삭제된 정보를 담을 스택
#
#     for c in cmd:
#         if c.startswith('U') or c.startswith('D'):
#             action, count = c.split()
#             # 숫자로 변환해서 그만큼 고리 이동
#             for _ in range(int(count)):
#                 k = table[k][0] if action == 'U' else table[k][1]
#
#         elif c == 'C':
#             prev, next = table[k]
#             deletes.append((prev, k, next)) # 복구용 정보 저장
#             results[k] = 'X'
#
#             # 앞뒤 연결 고리 수정 (나를 건너뛰게 만들기)
#             if prev is not None: table[prev][1] = next
#             if next is not None: table[next][0] = prev
#
#             # 다음 커서 위치 결정
#             k = next if next is not None else prev
#
#         elif c == 'Z':
#             p, curr, nxt = deletes.pop()
#             results[curr] = 'O'
#             # 앞뒤 노드에게 내가 돌아왔음을 알림
#             if p is not None: table[p][1] = curr
#             if nxt is not None: table[nxt][0] = curr
#
#     return "".join(results)
# --------------------------------------------------------------------------
