def is_able(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for current_s in s:
        # 1. 여는 괄호인 경우
        if current_s in pairs.values():
            stack.append(current_s)
        
        # 2. 닫는 괄호인 경우
        elif current_s in pairs:
            # 스택이 비었거나, 마지막으로 열린 괄호가 내 짝꿍이 아니면 실패
            if not stack or stack[-1] != pairs[current_s]:
                return False
            stack.pop() # 짝이 맞으므로 제거
            
    # 최종적으로 모든 괄호가 짝을 찾아 떠났는지(비었는지) 확인
    return len(stack) == 0

def solution(s):
    count_success = 0
    # 문자열 길이만큼 회전
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_able(rotated):
            count_success += 1
    return count_success