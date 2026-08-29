# 08_LV1_read_file_and_sum.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/d35dd5c25a48009c3badc2f3d3f2468a

## 2026-03-05

bug : int() 함수는 이 명단 전체를 한꺼번에 숫자로 바꿀 수 없기 때문에 명단에 있는 줄(line)을 하나씩 꺼내서 숫자로 바꾼 뒤 더해주는 과정이 필요

## 2026-03-05

fix : 공백에 대한 우려 -> strip으로 제거 필요
