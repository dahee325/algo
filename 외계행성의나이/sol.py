#아스키코드 활용
def solution(age):
    answer = []
    for num in str(age):
        answer.append(chr(int(num)+97))
    return ''.join(answer)
    # return ''.join([chr(int(num)+97) for i num in str(age)])


print(solution(23)) # => 'cd'
print(solution(51)) # => 'fb'
print(solution(100)) # => 'baa'