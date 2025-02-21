# 내 풀이
def solution(my_string, letter):

    # for char in letter:
    #     answer = my_string.replace(char, '')

    # return answer
    return my_string.replace(letter, '')



print(solution('abcdef', 'f')) # => abcde
print(solution('BCBdbe', 'B')) # => Cdbe