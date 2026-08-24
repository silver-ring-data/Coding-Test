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