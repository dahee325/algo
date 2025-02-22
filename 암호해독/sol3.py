def solution(cipher, code):
    return cipher[code-1::code]


print(solution('dfjardstddetckdaccccdegk', 4)) # => 'attack'
print(solution('pfqallllabwaoclk', 2)) # => 'fallback'