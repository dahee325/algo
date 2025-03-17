def solution(array, n):
    answer = []
    result = []
    for num in array:
        answer.append(abs(num-n))
        min_num = min(answer)
    for i, value in enumerate(answer):
        if value == min_num:
            result.append(array[i])
    return min(result)


print(solution([3, 1, 28], 20)) # => 28
print(solution([10, 11, 12], 13)) # => 12