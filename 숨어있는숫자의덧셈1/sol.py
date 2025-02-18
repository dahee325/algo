# 내 풀이
def solution(my_string):
    num = range(0, 10)
    answer = ''

    for i in my_string:
        if i in num:
            answer.append(i)

    return sum(answer)

#못 풀었당.....

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))