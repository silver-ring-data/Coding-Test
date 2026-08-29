def solution(id_list, report, k):
    infos = {reported_id : set() for reported_id in id_list} # {신고당한 유저 id : [신고한 유저 id list]}
    
    for current_report in report :
        user_id, reported_id = current_report.split()
        infos[reported_id].add(user_id)
        
    answer = [0] * len(id_list)
    for current_id in id_list : # id 리스트 불러오기
        if len(infos[current_id]) >= k : # current_id를 신고한 사람이 k번 이상이라면
            for reporter in infos[current_id]: # 신고자별로 카운트 올려주기
                answer[id_list.index(reporter)] += 1
    return answer

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/bf5d0344587d2e5a79f600957a4e81db
#
# [2026-04-12]
# 배운것 :
# - infos = {reported_id: set() for reported_id in id_list} : set를 안에 넣어서 만드는 것도 가능
# - list.index(value) : 특정값의 인덱스 찾기
#
# [2026-04-12]
# [opt]
#
# ```
# def solution(id_list, report, k):
#     # 1. {신고당한 유저: {신고한 유저들(set)}} 초기화
#     # set을 사용해 중복 신고를 자동으로 방지 (파이썬 코딩의 기술: 적절한 자료구조 선택)
#     infos = {reported_id: set() for reported_id in id_list}
#
#     for current_report in report:
#         user_id, reported_id = current_report.split()
#         infos[reported_id].add(user_id)
#
#     # 2. {유저 이름: 인덱스} 매핑 딕셔너리 생성
#     # 루프 안에서 .index()를 호출하는 O(n) 연산을 피하기 위함 (성능 최적화)
#     user_to_idx = {name: i for i, name in enumerate(id_list)}
#
#     answer = [0] * len(id_list)
#
#     # 3. 정지 유저 판별 및 메일 카운트 계산
#     for reported_id, reporters in infos.items():
#         if len(reporters) >= k:
#             # 정지된 유저를 신고한 사람들에게 메일 발송
#             for reporter in reporters:
#                 idx = user_to_idx[reporter]
#                 answer[idx] += 1
#
#     return answer
# ```
# --------------------------------------------------------------------------
