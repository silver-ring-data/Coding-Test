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

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/6b4b807d3629eeee8d1c8f3f90812c62
#
# [2026-03-22]
# [init] : 버그 없고 모두 성공이나, 로직에 허점이 있음. [({]형태는 못걸러냄
#
# [2026-03-22]
# [opt] : 로직 수정 및 딕셔너리를 괄호끼리 짝지어서 최적화
# 로직 수정 : 스택 리스트에 여는 괄호 닫는 괄호가 짝지어지는지 확인
# --------------------------------------------------------------------------
