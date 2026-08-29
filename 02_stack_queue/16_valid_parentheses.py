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

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/41b0b4aeb47146e781bc26e5e9408fe7
#
# [2026-03-18]
# [refactor] : 코드 간결화
#
# [2026-03-18]
# [opt]
# --------------------------------------------------------------------------
