# PCCP-Study

- 파일 이름 : **일자_레벨_문제 (**ex. 02_LV1_digit_reverse_list.py**)**
    - ex. 02_LV1_digit_reverse_list.py
- 파일 내용 : **코드내용 (함수정의 → Docstring → 코드 (주석)) → 피드백 내용 주석**
    - Docstring : (1) 요약 한 줄 → (2) 알고리즘 설명 → (3) 인자 설명 → (4) 반환값 설명
        - 예시
            
            ```python
            def calculate_area(radius):
                """원공의 넓이를 계산하여 반환함.  # (1) 요약 한 줄
            
                반지름 값을 받아 수학적 공식을 적용해 넓이를 구함. # (2) 상세 설명 (선택)
            
                Args: # (3) 인자 설명
                    radius (float): 원의 반지름 (양수여야 함).
            
                Returns: # (4) 반환값 설명
                    float: 계산된 원의 넓이.
                """
                import math
                return math.pi * (radius ** 2)
            ```
            
    - 단순 설명보다, **왜 이 방식을 선택**했는지
        - 예시
            
            ```python
            def solution(priorities: list[int], location: int) -> int:
                # ❌ 나쁜 주석: "큐에 데이터를 넣는다" (코드를 읽으면 알 수 있는 내용)
                # ✅ 좋은 주석: "인덱스 관리를 위해 enumerate를 사용해 (우선순위, 위치) 튜플 생성"
            ```
