def solution(nums):
    
    max_pokemon = len(nums)/2
    del_dup = len(list(set(nums)))
    
    # 만약 set해서 중복 제거후 2/N보다 작다면 그거 리턴
    if del_dup < max_pokemon:
        return del_dup
    
    if del_dup >= max_pokemon:
        return max_pokemon

    return answer

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/7e5807de169bbadfc0bc81dd178bf4ec
#
# [2026-04-24]
# [opt]
# ```
# def solution(nums):
#     pick_limit = len(nums) // 2
#     unique_types_count = len(set(nums))
#
#     # 두 값 중 최솟값 선택
#     # 이유: if-else 문보다 min()을 쓰면 "제한 사항 내에서 최선을 선택한다"는 의도가 명확해져.
#     return min(pick_limit, unique_types_count)
# ```
# --------------------------------------------------------------------------
