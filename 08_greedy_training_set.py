def solution(n, lost, reserve) -> int:
    total_list = [0] * n
    
    for reserve_value in reserve :
        total_list[reserve_value-1] += 1
        
    for lost_value in lost :
        total_list[lost_value-1] -= 1
        
    for index, value in enumerate(total_list) :
        if total_list[index] == 1 :
            for target in [index - 1, index + 1]:
                if 0 <= target < n and total_list[target] == -1:
        # 1. target이 리스트 범위(0 ~ n-1) 안에 있는지 확인
         # 2. 그리고 그 target 위치의 학생이 체육복이 없는지(-1) 확인
        
                        total_list[target] += 1  # 빌려줌
                        total_list[index] -= 1   # 내 여벌 소모
                        break  # 한 명에게 빌려줬으니 다음 학생으로 넘어감!
    result = 0       
    result += sum(1 for total in total_list if total != -1)
        
    return result