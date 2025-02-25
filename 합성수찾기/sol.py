def solution(n):
    answer = []
    count = 0
    for num in range(2, n+1):
        for i in range(1, num+1):
            if num % i  == 0:
                answer.append(num)
        if answer.count(num) >= 3:
            count += 1
    return count


print(solution(10)) # => 5
print(solution(15)) # => 8