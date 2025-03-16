def solution(n):
    answer = 1
    for i in range(1, 11):
        answer = answer*i
        if answer == n:
            return i
        elif answer > n:
            return i-1


print(solution(3628800)) # => 10
print(solution(7)) # => 3