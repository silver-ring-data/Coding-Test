def solution(cards1, cards2, goal):
    
    for goal_card in goal :
        issame = False
        if cards1:
            if goal_card == cards1[0] :
                cards1.pop(0)
                issame = True
        if cards2:
            if goal_card == cards2[0] :
                cards2.pop(0)
                issame = True
        if not issame :
            return "No"
        # 각 첫번째 요소들만 비교후
        # 없으면 No
        # 있으면 해당 리스트의 첫번째 요소 지우기
        
    return "Yes"

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/5eb09beab0b5b70eb5844e36e057d958
#
# [2026-03-31]
# [refact] :쓸모없는 변수할당 제거
# --------------------------------------------------------------------------
