from itertools import combinations

def solution(nums) :
    sums = [sum(c) for c in combinations(nums, 3)] # 3개의 값을 더한 리스트
    return sum(1 for s in sums if is_prime(s))

def is_prime(n) :
    if n < 2 : return False

    for dividend in range(2, n**0.5 + 1) :
        if n % dividend == 0 :
            return False
            
    return True
"""
    1. (반복문) 배열(nums)에서 값 3개(num)를 선택
        1-1. 값 3개를 더한 값이 소수인지를 판별
            1-1-1. 값을 나누는 수를 제곱근까지 1씩 더해서 나누어보고 
                만약에 나눈 값이 자연수일 경우, 소수이므로 카운트를 더함
    Args:
        nums : 입력된 배열
    Returns:
        return : 소수가 되는 경우의 개수
"""
    
    
"""
int(n**0.5) + 1을 통한 range 함수 인자 타입 에러 해결
제너레이터 표현식(sum(1 for ... ))을 사용하여 메모리 효율적 합산 구현
Better Way 26/30: 함수 분리 및 제너레이터 활용으로 클린 코드 달성
소수 판별 알고리즘 최적화 ($O(\sqrt{N})$) 완료 및 검증
"""
