def solution(my_string):
    answer = ''
    for string in my_string:
        if string == string.upper():
            answer += string.lower()
        else:
            answer += string.upper()
    return answer


print(solution('cccCCC')) # => 'CCCccc'
print(solution('abCdEfghIJ')) # => 'ABcDeFGHij'