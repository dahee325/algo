from math import sqrt

def solution(n):
    answer = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            answer.append(i)
            if i != n // i:
                answer.append(n // i)
    answer.sort()
    return answer


print(solution(24)) # => [1, 2, 3, 4, 6, 8, 12, 24]
print(solution(29)) # => [1, 29]