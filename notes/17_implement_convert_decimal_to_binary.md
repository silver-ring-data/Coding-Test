# 17_implement_convert_decimal_to_binary.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/cdfbac4e31f24eea6d0a1bf875fb7910

## 2026-03-19

이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

## 2026-03-19

[opt] : divmod 사용
- 일반적인 방식
quotient = 7 // 3  # 2
remainder = 7 % 3   # 1

- divmod 사용 방식
q, r = divmod(7, 3) 
print(q) # 2
print(r) # 1
