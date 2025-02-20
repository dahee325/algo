def solution(my_string, n):
    string = list(my_string)
    answer = []

    for i in string:
        answer.append(i * n)
    
    return ''.join(answer)

print(solution('hello', 3)) # => hhheeellllllooo