def solution(my_string):
    num = list(range(0, 10))
    answer = []
    for i in my_string:
        if i in num:
            answer.append(i)
    return answer

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))