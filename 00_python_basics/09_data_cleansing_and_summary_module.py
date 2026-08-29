import re

# 전체 처리량을 저장할 전역 변수
total_throughput = 0

def extract_user_id(log_text):
    """로그 텍스트에서 ID만 전문적으로 찾아주는 함수"""
    pattern = re.compile(r"ID:([A-Z]{3})")
    match = re.search(pattern, log_text)
    return match.group(1) if match else "Unknown"

def clean_throughput_data(data_list, threshold=10):
    """기준치 이상의 데이터만 걸러서 합계를 내주는 함수"""
    refined = [x for x in data_list if x >= threshold]
    return sum(refined), refined

def process_log_system(log_text, throughput_list):
    """메인 컨트롤러: 각 기능을 연결하고 전역 변수를 업데이트함"""
    global total_throughput
    
    # 1. ID 추출
    user_id = extract_user_id(log_text)
    
    # 2. 데이터 정제 (기준값 10)
    current_sum, cleaned = clean_throughput_data(throughput_list, 10)
    
    # 3. 전역 변수 업데이트
    total_throughput += current_sum
    
    return {
        "user_id": user_id,
        "current_sum": current_sum,
        "cleaned_data": cleaned,
        "total_accumulated": total_throughput
    }

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/14e576bcde0a299352ef8e6692e99b72
#
# [2026-03-06]
# [문제 상황]
# 당신은 데이터 엔지니어로서 여러 서버에서 모인 로그 데이터를 정제하는 함수를 작성해야 합니다.
# 로그 데이터에는 '사용자ID', '접속시간', '처리량'이 섞여 있습니다.
#
# [요구 사항]
# 전역 변수 활용: 전체 처리량을 누적 계산하기 위해 함수 외부의 total_throughput 변수를 함수 내부에서 수정할 수 있도록 설정하세요.
# 정규표현식 활용: 로그 문자열에서 대문자 알파벳 3자리로 된 사용자 ID만 추출하세요. (예: "ID:ABC" -> "ABC")
# 리스트 컴프리핸션 활용: 입력받은 throughput_list에서 10 이상인 수치만 골라내어 리스트를 만드세요.
# 결과 반환: 추출한 ID와 정제된 처리량 리스트의 합계를 반환하세요.
#
# log_text: "2026-03-06 16:00, SERVER_01, 리포트 생성, ID:GSW, 상태:완료"
# throughput_list: [1, 15, 3, 22, 9, 30, 5]
#
# [2026-03-06]
# [fix] : user_id가 GSW가 아니라 ID:GSW로 출력됨. -> 괄호사용할 것
#
# [2026-03-06]
# [bug fix] : global 과 연산은 한번에 처리 x -> 나누어서 사
#
# [2026-03-06]
# [opt] : 함수 나누기 및 리턴을 dict으로 처리하여 가독성과 확장성을 좋게 만듦.
# --------------------------------------------------------------------------
