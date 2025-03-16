def solution(emergency):
    answer = []
    sort_e = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(sort_e.index(i) + 1)
    return answer
    # return [sort.e.index(i) + for i in emergency]

print(solution([3, 76, 24])) # => [3, 1, 2]
print(solution([1, 2, 3, 4, 5, 6, 7])) # => [7, 6, 5, 4, 3, 2, 1]
print(solution([30, 10, 23, 6, 100])) # => [2, 4, 3, 5, 1]