def solution(s1, s2):
    return len(set(s1) & set(s2))


print(solution(['a', 'b', 'c'], ['com', 'b', 'd', 'p', 'c'])) # => 2
print(solution(['n', 'omg'], ['m', 'dot'])) # => 0