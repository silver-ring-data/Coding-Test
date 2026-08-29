# 06_LV1_unfinished_player.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/a56a9c389ac88f414a2a6d5e6096e3d9

## 2026-03-03

기존 방식: list.remove() 사용 시 $O(N^2)$ 발생 가능 (효율성 테스트 우려)
개선 제안: 1. dict를 활용해 빈도수 계산 ($O(N)$으로 단축)
2. collections.Counter 객체 간 차집합 연산 활용 (Pythonic Way)
3. 이유: 대규모 데이터 처리 시 시간 복잡도 최적화 및 코드 간결성 유지

## 2026-03-03

문제점: list.difference()는 존재하지 않으며, set 이용 시 동명이인 데이터 유실 발생.

해결 방안: collections.Counter를 사용하여 빈도수를 포함한 차집합 연산 수행.

클린 코드: 파이썬 내장 라이브러리를 활용해 복잡한 반복문 없이 직관적인 로직 구현.

## 2026-03-03

진행 상황: Counter 차집합을 통해 미완주자 선별 완료.

남은 작업: dict_keys 객체가 아닌 순수 문자열(String)로 결과값 추출.

클린 코드 포인트: iter()와 next()를 활용한 효율적인 데이터 추출 기법 적용 예정.

이유: 결과가 단 하나임을 보장할 때, 불필요한 리스트 변환 없이 값을 가져오기 위함.
