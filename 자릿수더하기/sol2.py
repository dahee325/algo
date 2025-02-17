def solution(n):
    answer = 0
    if n % 10 != 0:
        num = n // 10
        answer += n % 10
        if num % 10 != 0:
            num = n // 10
            answer += num % 10
        return answer


print(solution(1234))
print(solution(930211))

# 1의자리  : n을 10으로 나눈 나머지
# n을 10으로 나눈 몫을 10으로 나눈 나머지