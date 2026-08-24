def solution(s):
    count = 0
    for current_s in s :
        if current_s == '(':
            count += 1
        else :
            count -= 1
        
        if count < 0 :
            return False
    return count == 0