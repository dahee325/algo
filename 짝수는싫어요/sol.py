def solution(n):
    answer = []

    for num in range(1, n+1):
        if num % 2 != 0:
            answer.append(num)
        answer.sort()
    return answer
    # return [num for num range(1, n+1) if num % 2 == 1]
    # return [num for num in range(1, n+1, 2)]


print(solution(10)) # => [1, 3, 5, 7, 9]
print(solution(15)) # => [1, 3, 5, 7, 9, 11, 13, 15]