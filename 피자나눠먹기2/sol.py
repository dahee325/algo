# from math import lcm # 최소공배수

def solution(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = (6 * n) // gcd(6, n)
    return lcm // 6
    # return lcm(n, 6) // 6


print(solution(6)) # => 1
print(solution(10)) # => 5
print(solution(4)) # => 2