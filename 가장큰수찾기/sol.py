def solution(array):
    return [max(array), array.index(max(array))]


print(solution([1, 8, 3])) # => [8, 1]
print(solution([9, 10, 11, 8])) # => [11, 2]