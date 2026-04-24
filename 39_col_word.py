def solution(n, words):
    
    history = set([words[0]])
    
    # 두 번째부터 시작
    for i in range(1, len(words)):
        word = words[i]
        prev_word = words[i-1]
        
        # 탈락의 경우
            # 연결을 하지 못했을때
            # 중복된 단어를 말했을 때
        if word[0] != prev_word[-1] or word in history:
            
            person_num = (i % n) + 1 # 사람 번호
            turn_num = (i // n) + 1 # 각 사람의 단어 갯수
            
            return [person_num, turn_num]
        
        # 통과
        history.add(word)
        
    return [0, 0]