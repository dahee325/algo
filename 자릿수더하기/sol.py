#내 풀이
def solution(n):
    answer = 0
    while n < 10:
        if n % 10 != 0:
            answer += n % 10
            num = n // 10
        return answer


#내 풀이의 답
def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = n // 10
    return answer


print(solution(1234)) # => 10
print(solution(930211)) # => 16