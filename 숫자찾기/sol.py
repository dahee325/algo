def solution(num, k):
    answer = 0
    if str(k) in str(num):
        return str(num).index(str(k)) + 1
    else:
        return -1


print(solution(29183, 1)) # => 3
print(solution(232443, 4)) # => 4
print(solution(123456, 7)) # => -1