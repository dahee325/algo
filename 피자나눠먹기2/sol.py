def solution(n):
    answer = 0
    a, b = divmod(n, 6)
    while True:
        if b != 0:
            b = b % 6
            
        else:
            b == 0:
            return a

    

print(solution(6)) # => 1
print(solution(10)) # => 5
print(solution(4)) # => 2