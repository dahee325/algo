def solution(order):
    answer = 0
    numbers = '369'
    for num in str(order):
        if num in numbers:
            answer += 1
    return answer


print(solution(3)) # => 1
print(solution(29423)) # => 2