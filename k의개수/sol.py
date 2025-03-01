def solution(i, j, k):
    answer = 0
    numbers = range(i, j+1)
    for number in numbers:
        answer += str(number).count(str(k))
    return answer


print(solution(1, 13, 1)) # => 6
print(solution(10, 50, 5)) # => 5
print(solution(3, 10, 2)) # => 0