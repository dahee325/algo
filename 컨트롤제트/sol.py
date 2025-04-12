def solution(s):
    answer = []
    s = s.split(' ')
    for string in s:
        if string != 'Z':
            answer.append(int(string))
        else:
            answer.pop()
    return sum(answer)


print(solution('1 2 Z 3')) # => 4
print(solution('10 20 30 40')) # => 100
print(solution('10 Z 20 Z 1')) # => 1
print(solution('10 Z 20 Z')) # => 0
print(solution('-1 -2 -3 Z')) # => -3