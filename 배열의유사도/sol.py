def solution(s1, s2):
    answer = 0
    for string in s1:
        if string in s2:
            answer += 1
    return answer


print(solution(['a', 'b', 'c'], ['com', 'b', 'd', 'p', 'c'])) # => 2
print(solution(['n', 'omg'], ['m', 'dot'])) # => 0