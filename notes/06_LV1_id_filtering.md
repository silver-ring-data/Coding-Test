# 06_LV1_id_filtering.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/70d97eaebe9abd4b21d67f5994e82361

## 2026-03-03

타입 힌트 불일치: 

순서 보장(정렬): 아까 우리가 고민했듯이 set은 순서가 제멋대로야. 문제 요구사항인 **'알파벳 순서 정렬'**을 만족하려면 list(new_ids) 대신 **sorted(new_ids)**를 쓰는 게 좋아. sorted()는 결과를 알아서 리스트로 돌려주거든!
