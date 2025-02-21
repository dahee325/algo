def solution(hp):
    # a, b = divmod(hp, 5)
    # if b == 0:
    #     return a
    # else:
    #     if b < 3:
    #         return a + b
    #     else:
    #         return a + b % 3 + 1
    
    return hp // 5 + (hp % 5 // 3) + (hp % 5 % 3)


print(solution(23)) # => 5
print(solution(24)) # => 6
print(solution(999)) # => 201