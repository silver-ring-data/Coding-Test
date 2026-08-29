def solution(board, moves):

    buckets = []
    answer = 0 # 인형 터진 횟수
    for move in moves :
        col = move - 1 
        for row in range(len(board)):
            doll_number = board[row][col]
            
            if doll_number : #0이 아닐때
                if buckets and buckets[-1] == doll_number: # 비어있지 않으면서 마지막 인형 종류가 같을때
                    buckets.pop() # 제거
                    answer += 2 
                else : 
                    buckets.append(doll_number)
                
                board[row][col] = 0
                
                break # 집으면 끝
        
    return answer

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/f341a55f9d1928dfd4bd69bf096f37ad
#
# [2026-03-25]
# init 잘 돌아가는데, zip을 활용할 곳이 보임
#
# [2026-03-25]
# zip과 직관적인 열 기반 스택을 활용해서 리펙토링한 결과
#
# def solution(board, moves):
#     # 1. 각 열을 스택으로 변환 (0은 제외하고, 위에서부터 꺼내기 좋게 뒤집기)
#     # [list(row) for row in zip(*board)] -> 열 단위로 묶기
#     # [doll for doll in col if doll != 0] -> 0 제외
#     # [::-1] -> pop()을 썼을 때 위에서부터 나오도록 뒤집기
#     columns = []
#     for col in zip(*board):
#         # 0이 아닌 인형들만 모아서 역순으로 저장 (스택의 top이 인형 뽑기의 맨 위가 됨)
#         stack = [doll for doll in col if doll != 0][::-1]
#         columns.append(stack)
#
#     buckets = []
#     answer = 0
#
#     for move in moves:
#         index = move - 1
#         # 2. 해당 열에 인형이 있다면 스택에서 pop!
#         if columns[index]:
#             doll = columns[index].pop()
#
#             # 3. 바구니 로직 (이건 아까랑 같아!)
#             if buckets and buckets[-1] == doll:
#                 buckets.pop()
#                 answer += 2
#             else:
#                 buckets.append(doll)
#
#     return answer
# --------------------------------------------------------------------------
