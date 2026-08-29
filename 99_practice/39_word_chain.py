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

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/5b49b3477cda489bbf6be6349081fb57
#
# [2026-04-26]
# history = set([words[0]]) -> 처음에 set(words[0])로 썼었음.
# 불필요한 인덱싱 제거 후 enumerate 도입으로 최적화
# --------------------------------------------------------------------------
