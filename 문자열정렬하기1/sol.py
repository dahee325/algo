def solution(my_string):
    answer = []
    for string in my_string:
        if string.isdigit():
            answer.append(int(string))
            answer.sort()
    return answer


print(solution('hi12392')) # => [1, 2, 2, 3, 9]
print(solution('p2o4i8gj2')) # => [2, 2, 4, 8]
print(solution('abcde0')) # => [0]