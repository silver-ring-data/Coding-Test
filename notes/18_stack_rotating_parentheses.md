# 18_stack_rotating_parentheses.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/6b4b807d3629eeee8d1c8f3f90812c62

## 2026-03-22

[init] : 버그 없고 모두 성공이나, 로직에 허점이 있음. [({]형태는 못걸러냄

## 2026-03-22

[opt] : 로직 수정 및 딕셔너리를 괄호끼리 짝지어서 최적화
로직 수정 : 스택 리스트에 여는 괄호 닫는 괄호가 짝지어지는지 확인
