def solution(record):
    
    answer = []
    user_db = {}  # {status, id, name}
    
    # 1단계: Enter와 Change일 때
    for line in record:
        parts = line.split()
        status = parts[0]
        uid = parts[1]
        
        if status in ["Enter", "Change"]:
            nickname = parts[2]
            user_db[uid] = nickname

    # 2단계: 출력 메시지 (Enter, Leave 일때)
    for line in record:
        parts = line.split()
        status = parts[0]
        uid = parts[1]
        
        if status == "Enter":
            answer.append(f"{user_db[uid]}님이 들어왔습니다.")
        elif status == "Leave":
            answer.append(f"{user_db[uid]}님이 나갔습니다.")
            
    return answer