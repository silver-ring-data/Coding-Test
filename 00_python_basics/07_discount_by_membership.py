def function(price : int, current_member_class : str):
  member_discounts = [('Gold', 0.1), ('Silver', 0.05), ('Basic', 0.00)]

  final_price = price
  final_discount_rate = 0
  if price == 0:
    return # 프로그램 즉시 종료
  
  final_discount_rate = next((discount_rate for member_class, discount_rate in member_discounts if current_member_class == member_class),0.0)
  if final_discount_rate == 0.0 and current_member_class != 'Basic':
    print("해당되는 등급이 없습니다.")
  else :
    final_price = price*(1-final_discount_rate)
    return

  print(f'최종 결제 금액은 {final_price}원입니다.\n'.strip())
  if final_price >= 10000:
    print('사은품 증정\n'.strip())

price = int(input('주문 총액을 입력하세요\n').strip())
current_member_class = str(input('회원 등급을 입력하세요\n').strip())
function(price, current_member_class)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/85ee3246f3fa35c0b09cdd749fed3033
#
# [2026-03-04]
# 반복문(for)의 사용: 불필요
#
# 삼항 연산자 적용: 문제 요구사항이었던 삼항 연산자를 사용하면 코드가 훨씬 간결해질 거야.
#
# [2026-03-04]
# final_price부분의 문구가 잘못됨 제너레이터를 연산할 수 없음
#
# [2026-03-04]
# next 구문을 넣어서 제너레이터에 대한 부분은 해결했으나, 예외처리의 타입을 이상하게 해서 에러가 남.
# 출력을 동일한 타입으로 맞추고 예외처리는 다른 구문에서 해결해야할 것으로 보임
# --------------------------------------------------------------------------
