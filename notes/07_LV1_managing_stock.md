# 07_LV1_managing_stock.py — 풀이 메모

> gist 코멘트 이관 (2026-08-29). 원본: https://gist.github.com/silver-ring-data/a351108139fd90aafca60a547b1704df

## 2026-03-04

for menu, price, stock in order.values() 부분에서 버그 : 딕셔너리 한개인데, 반복문을 돌리고 있었음.

## 2026-03-04

[add] : available_menus 에 대한 문구 추가. 버그 발생 : 리스트가 아니라 딕셔너리기 때문에 index로 안받음.
