def solution(my_string):
    answer = []
    for i in range(0, len(my_string)):
        if my_string[i].isdigit():
            if i == 0:
                answer.append(int(my_string[0]))
            elif my_string[i-1].isdigit():
                answer.append(int(''.join([my_string[i-1], my_string[i]])))
            else:
                answer.append(int(my_string[i]))
    return sum(answer)


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))