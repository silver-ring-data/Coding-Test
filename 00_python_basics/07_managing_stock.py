def function(orders : list) -> str :
  for order in orders :
    menu, price, stock = order.values()
    if stock :
      print(f'{menu} 가격: {price}원 (재고: {stock})')
    else :
      continue

  available_menus = [order['menu'] for order in orders if order['stock']]
  print(available_menus)
  return 
orders = [
{'menu': '아메리카노', 'price': 4000, 'stock': 5},
{'menu': '카페라떼', 'price': 4500, 'stock': 0},
{'menu': '자몽허니블랙티', 'price': 5500, 'stock': 3},
{'menu': '바닐라라떼', 'price': 5000, 'stock': 0}
]

function(orders)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/a351108139fd90aafca60a547b1704df
#
# [2026-03-04]
# for menu, price, stock in order.values() 부분에서 버그 : 딕셔너리 한개인데, 반복문을 돌리고 있었음.
#
# [2026-03-04]
# [add] : available_menus 에 대한 문구 추가. 버그 발생 : 리스트가 아니라 딕셔너리기 때문에 index로 안받음.
# --------------------------------------------------------------------------
