from math import sqrt

def solution(n):
    if n % sqrt(n) == 0:
        return 1
    else:
        return 2
    # return 1 if n % sqrt(n) == 0 else 2


print(solution(144)) # => 1
print(solution(976)) # => 2