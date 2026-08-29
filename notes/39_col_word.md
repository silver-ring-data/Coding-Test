# 39_col_word.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/5b49b3477cda489bbf6be6349081fb57

## 2026-04-26

history = set([words[0]]) -> 처음에 set(words[0])로 썼었음.
불필요한 인덱싱 제거 후 enumerate 도입으로 최적화
