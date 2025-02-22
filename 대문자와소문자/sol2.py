def solution(my_string):
    return my_string.swapcase() # 문자열의 대소문자를 서로 바꿔주는 함수


print(solution('cccCCC')) # => 'CCCccc'
print(solution('abCdEfghIJ')) # => 'ABcDeFGHij'