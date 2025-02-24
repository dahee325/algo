def solution(n):
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1


print(solution(7)) # => 1
print(solution(1)) # => 1
print(solution(15)) # => 3