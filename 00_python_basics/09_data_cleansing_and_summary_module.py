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