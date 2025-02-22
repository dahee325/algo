from math import lcm # 최소공배수

def solution(n):
    return lcm(n, 6) // 6


print(solution(6)) # => 1
print(solution(10)) # => 5
print(solution(4)) # => 2

# 코드는 돌아가는데 정답인정이 안됌..