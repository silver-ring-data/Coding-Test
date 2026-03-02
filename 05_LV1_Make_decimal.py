from itertools import combinations

def solution(nums) :
    """
    1. (반복문) 배열(nums)에서 값 3개(num)를 선택
        1-1. 값 3개를 더한 값(sum_num)이 소수인지를 판별
            1-1-1. (반복문) sum_num을 sum_num-1부터 2까지 1씩 내려가면서 차례대로 나눔
                만약에 나눈 값이 자연수일 경우, 소수이므로 카운트를 더함
    Args:
        nums : 입력된 배열
    Returns:
        return : 소수가 되는 경우의 개수
    """

    sums = [sum(c) for c in combinations(nums, 3)] # 3개의 값을 더한 리스트
    count_sums = len(sums)
    
    count_not_prime = counting_not_prime(sums)
    
    answer = count_sums - count_not_prime # 전체 - 소수가 아닌 경우
    return answer

def counting_not_prime (sums) :
    count_not_prime = 0
    for sum_num in sums :
        dividend = sum_num - 1 # 소수를 판별할 나누는 수 정의.
        while dividend >= 2 :# 2까지만 나누기
            if is_not_prime(sum_num, dividend) == True :
                count_not_prime += 1
                break
            dividend -= 1 # 나누는 수 -1
    return count_not_prime

def is_not_prime(sum_num, dividend) :
    if sum_num % dividend == 0 : # 소수가 아님
        return True
    else :
        return False
    
    
"""
true, false가 아니라 첫 글자가 대문자인 True, False를 사용
"""
