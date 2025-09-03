# 10 진수를 2진수로 변환
def deciaml_to_binary(n):
    # 반복문
    binary_number = ""

    if n == 0:
        return "0"
    
    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        # 문자열을 앞에서 더해주면 reverse안해도 됨 / 나머지를 밑에서부터 거꾸로 읽어야하는데 앞으로 더해주면 자동으로 거꾸로 읽어짐
        binary_number = str(remain) + binary_number
        n //= 2     # n = n // 2 

    return binary_number
    # 재귀호출로는 어떻게?

# 10 진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    # 여러개의 데이터를 변화 없이 조회만 해야하는 경우 문자열이 빠르다.
    # 만약 변화가 있다면 리스트, 딕셔너리를 이용
    hex_digits = "0123456789ABCDEF" 
    hexadecimal_number = ""
        
    if n == 0:
        return 0

    # 0보다 클 때까지 16으로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 16
        # 10 ~ 15를 A ~ B로 변환
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n //= 16

    return hexadecimal_number

# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        # 1인 경우만 계산해주면 된다.
        if digit == "1":
            decimal_number += 2 ** pow
        # power를 for문이 동작할 때 마다 올려준다.
        pow += 1

    return decimal_number

