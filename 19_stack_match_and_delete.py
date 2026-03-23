def solution(s):
    stack = []
    
    for char in s:
        # 스택에 무언가 있고, 맨 위 글자가 현재 글자와 같다면? -> 짝꿍 발견!
        if stack and stack[-1] == char:
            stack.pop()
        # 그 외의 모든 경우 (스택이 비었거나, 글자가 다르거나) -> 일단 쌓기
        else:
            stack.append(char)
            
    # 스택이 비어있으면 1(성공), 남아있으면 0(실패)
    return 1 if not stack else 0