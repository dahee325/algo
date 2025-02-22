def solution(cipher, code):
    answer = []
    for i in range(code - 1, len(cipher), code):
        answer.append(cipher[i])
    return ''.join(answer)
    # return ''.join([cipher[i] for i in range(code - 1, len(cipher), code)])


print(solution('dfjardstddetckdaccccdegk', 4)) # => 'attack'
print(solution('pfqallllabwaoclk', 2)) # => 'fallback'