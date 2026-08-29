# 13_implement_matrix_multiplication.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/ae4ca3ef4e50449a36128d1fdaa1c160

## 2026-03-15

2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

## 2026-03-15

opt : zip을 활용해서 최적화를 할수도 있으나, 이런 문제는 정확한 인덱싱이 중요하기 때문에 원래 썼던 답도 괜찮은 코드.
- zip(*matrix)를 활용한 전치(Transpose) : arr2의 열을 한꺼번에 튜플로 가지고 올 수있기 때문에 코드가 간결해짐
