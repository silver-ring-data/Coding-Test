# 08_LV1_hate_same_num.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/74a14ee65922d6837788bcc33a40fcd1

## 2026-03-05

생각해봐야할 부분
1. 반복문의 시작점
2. if-else 구조의 단순화
3. 불필요한 변수 정의

## 2026-03-05

1. next(...) 문구로 리스트의 원소가 2개밖에 할당되지 않음 -> enumerate 도입고려

## 2026-03-05

arr[0]일때 문제 발생 : arr[index-1]에서 arr[-1]이 되어 비교가 이상하게 됨. -> 예외처리 필요

## 2026-03-05

arr[index] vs value 비교 : arr[index]는 다시 주소를 찾아서 가야하지만, value는 이미 할당이 되어있어 더 빠름
