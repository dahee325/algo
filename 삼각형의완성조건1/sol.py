def solution(sides):
    sides.sort()

    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2


print(solution([1, 2, 3])) # => 2
print(solution([3, 6, 2])) # => 2
print(solution([199, 72, 222])) # => 1