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