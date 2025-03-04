def solution(before, after):
    answer = []
    for string in list(before):
        answer = answer.insert(string, 0)
    return answer


print(solution('olleh', 'hello'))
print(solution('allpe', 'apple'))