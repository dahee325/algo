def solution(strlist):
    return [len(i) for i in strlist]

print(solution(["We", "are", "the", "world!"])) # => [2, 3, 3, 6]
print(solution(["I", "Love", "Programmers."])) # => [1, 4, 12]