def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer


print(solution('dfjardstddetckdaccccdegk', 4)) # => 'attack'
print(solution('pfqallllabwaoclk', 2)) # => 'fallback'