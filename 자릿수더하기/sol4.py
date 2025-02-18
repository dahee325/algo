def solution(n):
    return sum(map(int, list(str(n))))
                    # list(str(n)) => ['1', '2', '3', '4']
                # map(list(str(n))) => 1, 2, 3, 4
            # sum(map(list(str(n)))) => 10

print(solution(1234)) => 10
print(solution(930211)) => 16