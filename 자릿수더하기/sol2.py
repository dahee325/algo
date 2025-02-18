# 선생님풀이
def solution(n):
    answer = 0
    while n > 0:
        a, b = divmod(n, 10)
        # a = divmod(n, 10)[0] = n // 10 => 몫
        # b = divmod(n, 10)[1] = n % 10 => 나머지

        answer = answer + b
        n = a

    return answer


print(solution(1234))
print(solution(930211))