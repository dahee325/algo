def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

    return [my_str[i:i+n] for i range(0, len(my_str), n)]


print(solution('abc1Addfggg4556b', 6)) # => ['abc1Ad', 'dfggg4', '556b']
print(solution('abcdef123', 3)) # => ['abc', 'def', '123']