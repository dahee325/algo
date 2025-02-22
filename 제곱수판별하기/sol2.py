def solution(n):
    # if (n ** 0.5).is_integer():
    #     return 1
    # else:
    #     return 2
    return 1 if (n ** 0.5).is_integer() else 2


print(solution(144)) # => 1
print(solution(976)) # => 2