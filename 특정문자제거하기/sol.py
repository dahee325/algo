# 내 풀이
def solution(my_string, letter):

    for char in letter:
        answer = my_string.replace(char, '')

    return answer


print(solution('abcdef', 'f')) # => abcde
print(solution('BCBdbe', 'B')) # => Cdbe