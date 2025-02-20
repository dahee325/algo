def solution(num_list):
    a = []
    b = []
    for num in num_list:
        if num % 2 == 0:
            a.append(num)
        else:
            b.append(num)
    return [len(a), len(b)]


print(solution([1, 2, 3, 4, 5])) # => [2, 3]
print(solution([1, 3, 5, 7])) # => [0, 4]