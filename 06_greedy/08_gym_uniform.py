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

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/27a82099ec55e1c416ffd66fd1b7f4f8
#
# [2026-03-06]
# [문제 설명]
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
#
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
#
# [2026-03-10]
# [fix] : 실행은 되나, 로직의 허점이 몇몇 보임.
# 1. [index-1, index+1] 처럼 리스트를 직접 선언하여 가독성 향상
# 2. if 0 <= target < n: 조건을 통해 인덱스 에러(IndexError) 사전 방지
# --------------------------------------------------------------------------
