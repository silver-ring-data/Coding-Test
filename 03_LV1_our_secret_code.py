def solution(s: str, skip: str, index: int) -> str:
    # 1. 사용할 수 있는 알파벳만 골라낸 '안전한 사전'을 만들기
    # set을 활용해 skip 문자를 O(1) 속도로 필터링 (파이썬 코딩의 기술 - 효율적인 알고리즘 선택)
    skip_set = set(skip)
    valid_alphabets = [char for char in string.ascii_lowercase if char not in skip_set]
    
    # 2. 문자를 인덱스로 빠르게 찾기 위한 딕셔너리 생성 (속도 최적화)
    char_to_idx = {char: i for i, char in enumerate(valid_alphabets)}
    pool_size = len(valid_alphabets)
    
    result = []
    for char in s:
        # 3. 현재 문자의 위치에서 index만큼 더한 뒤, 나머지 연산(%)으로 순환 처리
        # (파이썬 코딩의 기술 - 복잡한 식을 작은 함수나 단계로 나누기)
        current_idx = char_to_idx[char]
        new_idx = (current_idx + index) % pool_size
        result.append(valid_alphabets[new_idx])
    
    # 4. 리스트를 문자열로 합치기
    return "".join(result)
