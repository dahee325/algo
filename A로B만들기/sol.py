def solution(before, after):
    for string in before:
        if before.count(string) == after.count(string):
            pass
        else:
            return 0
    return 1

print(solution('olleh', 'hello')) # => 1
print(solution('allpe', 'apple')) # => 0
