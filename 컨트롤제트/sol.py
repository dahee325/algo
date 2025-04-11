def solution(s):
    answer = 0
    s = s.split(' ')
    for number in range(0, len(s)):
        if s[number] == 'Z':
            s.remove(s[number-1])
    return s


print(solution('1 2 Z 3')) # => 4
print(solution('10 20 30 40')) # => 100
print(solution('10 Z 20 Z 1')) # => 1
print(solution('10 Z 20 Z')) # => 0
print(solution('-1 -2 -3 Z')) # => -3