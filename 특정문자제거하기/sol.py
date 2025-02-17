def solution(my_string, letter):
    for char in letter:
        answer = my_string.replace(char, '')

    return answer

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))