def decimal_to_binary(number):

    remainders = []
    while number > 0:
        # divmod를 사용하여 몫과 나머지를 한 번에 계산
        number, remainder = divmod(number, 2)
        remainders.append(str(remainder))

    # 리스트를 뒤집고 문자열로 합침
    return "".join(remainders[::-1])