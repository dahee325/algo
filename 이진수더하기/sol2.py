def solution(bin1, bin2):
    # int(bin1, 2) : 2진수를 10진수로 변환
    # bin() : 10진수를 2진수로 변환환
    a = int(bin1, 2) + int(bin2, 2)
    return bin(a)[2:]


print(solution('10', '11')) # => '101'
print(solution('1001', '1111')) # => '11000'