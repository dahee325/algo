def solution(my_string):
    return ''.join(sorted(list(my_string.lower())))


print(solution('Bcad')) # => 'abcd'
print(solution('heLLo')) # => 'ehllo'
print(solution('Python')) # => 'hnopty'