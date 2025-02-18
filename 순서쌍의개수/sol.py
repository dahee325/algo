def solution(n):
    answer = 0

    for a in range(1, n+1):
        if n % a == 0:
            answer += 1

    return answer


print(solution(20))
print(solution(100))