def solution(hp):
    answer = 0

    for i in [5, 3, 1]:
        a, hp = divmod(hp, i)
        answer += a
    return answer


print(solution(23)) # => 5
print(solution(24)) # => 6
print(solution(999)) # => 201