def solution(nums):
    
    max_pokemon = len(nums)/2
    del_dup = len(list(set(nums)))
    
    # 만약 set해서 중복 제거후 2/N보다 작다면 그거 리턴
    if del_dup < max_pokemon:
        return del_dup
    
    if del_dup >= max_pokemon:
        return max_pokemon

    return answer