def solution(my_string):
    num = ['0','1','2','3','4','5','6','7','8','9']
    answer = 0

    for i in range(len(my_string)):
        if my_string[i] in num:
            answer += int(my_string[i])
        # else:
        #     continue
    return answer


print(solution('aAb1B2cC34oOp')) # => 10
print(solution('1a2b3c4d123')) # => 16