def solution(my_string):
    answer = ''
    for string in my_string:
        if string not in answer:
            answer += string
    return answer


print(solution('people')) # => 'peol'
print(solution('We are the world')) # => 'We arthwold'