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