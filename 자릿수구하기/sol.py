def solution(n):
    answer = 0
    while n <10:
        if n % 10 != 0:
            answer += n % 10
            n = n // 10
        return answer


print(solution(1234))
print(solution(930211))