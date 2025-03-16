def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    else:
        return 0


print(solution('olleh', 'hello')) # => 1
print(solution('allpe', 'apple')) # => 0