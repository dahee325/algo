def solution(sides):
    if max(sides) < sum(sides) - max(sides):
        return 1
    else:
        return 2


print(solution([1, 2, 3])) # => 2
print(solution([3, 6, 2])) # => 2
print(solution([199, 72, 222])) # => 1